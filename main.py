from model.kuran import Kuran
from ml import csv_generator, huruf_word_count


############################################################
''' File generation
csv_generator.CsvGenerator().generate()
'''
############################################################
''' General overview 
kuran = Kuran()
sure_with_single_huruf = kuran.get_sure_with_single_huruf()
huruf_sure_dict = kuran.get_huruf_sure_dict()
sure_analysis = kuran.get_sure_and_huruf_analysis()
huruf_tuple_sure = kuran.get_huruf_tuple_sure_dict()
huruf_tuple_alphabet_order = kuran.get_huruf_tuple_alphabet_order()
x = 1
'''
############################################################
''' HTML '''

huruf_word_count.HurufWordCount().execute()