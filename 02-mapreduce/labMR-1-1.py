from mrjob.job import MRJob

class averageSalary_se(MRJob):

    def mapper(self, _, line):
        idemp, sececon, salary, year = line.split(',')
        try:
         salary = int(salary)
        except ValueError:
         pass
        else:
         yield sececon, salary

    def reducer(self, key, values):
        total = 0
        cantidad = 0
        for salary in values:
         total = total + salary
         cantidad = cantidad + 1
        yield key, total/cantidad

if __name__ == '__main__':
    averageSalary_se.run()
