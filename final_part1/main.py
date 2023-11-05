import csv
import os
import random


class CSVData:
    def __init__(self, filepath, separator=','):
        self.filepath = filepath
        self.separator = separator
        self.data = list(csv.reader(open(filepath, encoding='utf-8-sig'), delimiter=separator))
        self.header = self.data[0]
        self.rows = self.data[1:]

    def Show(self, output_type='top', num_rows=5):
        if len(self.rows) < num_rows:
            print("Cтрок недостаточно")
            num_rows = len(self.rows)

        if output_type == 'top':
            rows = self.rows[:num_rows]
        elif output_type == 'bottom':
            rows = self.rows[-num_rows:]
        elif output_type == 'random':
            rows = random.sample(self.rows, num_rows)
        else:
            print("Неверный тип вывода('top', 'bottom', and 'random')")
            return

        print(','.join(self.header))
        for row in rows:
            print(','.join(row))

    def Info(self):
        print(f'{len(self.rows)}x{len(self.header)}')
        for i, name in enumerate(self.header):
            non_empty_values = len([row[i] for row in self.rows if row[i] != ''])
            try:
                value_type = type(int(self.rows[0][i])).__name__
            except ValueError:
                try:
                    value_type = type(float(self.rows[0][i])).__name__
                except ValueError:
                    value_type = type(self.rows[0][i]).__name__
            print(f'{name} {non_empty_values} {value_type}')

    def DelNaN(self):
        self.rows = [row for row in self.rows if all(cell != '' for cell in row)]

    def makeDS(self):
        random.shuffle(self.rows)
        split_index = int(0.7 * len(self.rows))
        train_data = self.rows[:split_index]
        test_data = self.rows[split_index:]

        if not os.path.exists('workdata/Learning'):
            os.makedirs('workdata/Learning')
        if not os.path.exists('workdata/Testing'):
            os.makedirs('workdata/Testing')

        with open('workdata/Learning/train.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(self.header)
            writer.writerows(train_data)

        with open('workdata/Testing/test.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(self.header)
            writer.writerows(test_data)


data = CSVData('data.csv')
data.Show('top', 5)
data.Show('bottom', 5)
data.Show('random', 5)
data.Info()
data.DelNaN()
data.makeDS()
