# bachelor_diploma
Бакалаврская работа
студентки группы M3437
Звягинцевой Дарьи
Университет ИТМО
2020г


Для запуска файлов необходимо загрузить исходные данные. Они доступны на гугл-диске по ссылке:
https://drive.google.com/open?id=1TqNBD7yCKF3o6PXxWaOCYBH4iMMyp4mI


# Краткое описание файлов.


Предобработка:
1.  filter_data.py - фильтрация осцилирующих данных
2.  invert_data.py - инвертация некоторых решеток, чтобы зеркальные отображения одной фазы не мешали алгоритмам

Генерация файлов:

1. generate_wj.py - генерация файлов с параметром накачки и коэффициентом связи между узлами
2. gen_snz.py - генерация файлов с значение намагниченности 
3. particuly_label.py - частичная разметка данных данных для оценки agglomarative clustering

Генерация картинок:
1. gen_lattice.py - генерация иллюстраций решеток
2. gen_pictures_for_presentation.ipynb - генерация картинок, для объяснения метода learning by confusion
3. gen_phase_diagram.py -  генерация первого приближения фазовой диаграммы
4. final_plot.ipynb - генерация фазовой диаграммы с межфазовыми границами (по данным, полученным от learning by confusion)

Методы машинного обучения:
1. gen_TSNE.py - генерация tSNE с оценкой качетва
2. agglomerative_quality.ipynb - генерация agglomerative clustering с оценкой качетва
3. learning_by_confusion.ipynb -  learning by confusion


