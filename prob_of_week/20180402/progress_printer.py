#! /bin/env python3
import sys

class Progress_printer :
	
	def print_progress(self, iteration, total, prefix='Progress:', suffix='Complete', decimals=10, bar_length=50):

		str_format = "{0:." + str(decimals) + "f}"
		percents = str_format.format(100 * (iteration / float(total)))
		filled_length = int(round(bar_length * iteration / float(total)))
		bar = '█' * filled_length + '-' * (bar_length - filled_length)

		sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percents, '%', suffix)),

		if iteration == total:
			sys.stdout.write('\n\n')
		sys.stdout.flush()
