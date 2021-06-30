This is a backend part of the Auction project.

The application requires a PostrgreSQL service. After that, you need to define the environment variables from the `example.env` file according to your environment.

To start the project, you need to install dependencies from the `requirements.txt` file and start the server using the `uwsgi --ini uwsgi.ini` command or use the Docker image of the application from the registry of the project.


В связи с болезнью и ограниченным временем решил остановиться на том что есть. Если говорить о том что бы я добавил в данном задании, это в первую очередь тесты, в модели Bet добавил бы поле step в котором бы хранил минимальный шаг ставки. Так же это всё нужно валидировать и проверять какая ставка была выставлена, не меньше ли она текущей ставки, соответствует ли она минимальному шагу. Добавил различного рода фильтры на вьюхи для того что бы пользователи моги фильтровать лоты по тем или иным параметрам (к примеру по породе или типу котик/ёжик). Фильтрация своих (и не только) лотов по статусам, для возможности видеть новые лоты и которые будут активны в ближайшее время (хорошая идея добавить дату старта лота) Прикрутил селери и редис для возможности рассылки сообщений юзерам, которые к примеру выиграли лот или рассылке любых других сообщений.