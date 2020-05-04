from mrjob.job import MRJob

class seNumber_employee(MRJob):

    def mapper(self, _, line):
        idemp, sececon, salary, year = line.split(',')
        yield (idemp, (sececon, 1))

    def reducer(self, key, values):
        total = 0
        for sececon, count in values:
         total = total + count
        yield key, total

if __name__ == '__main__':
     seNumber_employee.run()
