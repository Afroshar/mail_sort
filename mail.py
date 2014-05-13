# -*- coding: utf-8 -*-
import sys
import os

'''
За каждый проход обрабатывается первое письмо, и все последующие с таким же адресом.
Обработанные письма удаляются из буфера.
'''
def split( data ):
    if not os.path.exists("c:\sorted_mail"):
        os.makedirs("c:\sorted_mail")
    while data.find( "\nFrom " ) != -1:
        addr_beg = data.find( "\nFrom " ) + 6
        addr_end = data.find( " ", addr_beg )
        current_addr = data[addr_beg:addr_end]
        addr_end = 0
        mail_count = 0
        with open("c:\sorted_mail\\" + current_addr + ".mailbox", mode="w", encoding="utf-8") as current_file:
            while data.find( "\nFrom ", addr_end ) != -1:
                addr_beg = data.find( "\nFrom ", addr_end ) + 6
                addr_end = data.find( " ", addr_beg )
                if (data[addr_beg:addr_end] == current_addr):
                    mail_end = data.find( "\nFrom ", addr_end )
                    current_file.write( data[addr_beg-6:mail_end] )
                    data = data[:addr_beg-6] + data[mail_end:]
                    addr_end = addr_beg-6
                    mail_count += 1
            print("File: " + current_file.name + "\t" + "Mail count: " + str(mail_count))
              
with open(sys.argv[1]) as main_file:
    split("\n" + main_file.read())
