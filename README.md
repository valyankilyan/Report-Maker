# Report Maker
Утилита, которая поможет вам составить отчет для сдачи работ в первом неклассическом.

# Запуск
Перед запуском убедитесь, что у вас установлен python 3 и pip 3.
Также необходимо, чтобы был установлен npm.

```bash
python docxreplacer.py
doc2pdf out.docx
markdown-pdf <PATH.md>
pdfunite out.pdf <PATH.md> <PATH_OUT>
```

## Перед первым запуском
``` bash
pip install -r requirements
sudo npm install markdown-
sudo apt install unoconv
sudo apt install poppler-utils
```


## Титульный лист
``` bash
python docxreplacer.py
```

### Замена параметров
Все параметры на данный момент хранятся в файле `title_keys`. Для того, чтобы изменить или добавить свои, отредактируйте `title_template.docx` и `title_keys` в нужных местах.

## Генератор md to pdf
```bash
markdown-pdf <PATH>
```

## Генератор docx to pdf
```bash
doc2pdf <PATH>
```

## Мержим два pdf файла
```bash
pdfunite <PATH_0> <PATH_1> <PATH_OUT>
```
