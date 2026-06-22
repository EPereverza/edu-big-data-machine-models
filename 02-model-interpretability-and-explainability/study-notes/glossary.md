# Глоссарий незнакомых вещей (обязательно)

Обновляйте этот файл **по ходу выполнения** ноутбуков, а не в конце.

Минимальные требования:
- добавить не менее 3 новых терминов на каждый ноутбук;
- для каждого термина указать простое объяснение своими словами;
- указать, где термин встретился в работе;
- добавить источник (URL, учебник, статья или ссылка на внутреннюю заметку).

| Термин | Простое объяснение своими словами | Где встретился в ЛР | Источник |
|---|---|---|---|
| `Global importance` | Общая картина того, какие признаки в среднем сильнее влияют на решение модели. | Notebook 1, раздел глобальных объяснений. | Interpretable ML (Molnar), chapter on feature importance. |
| `Partial Dependence` | Показ, как меняется средний score модели при изменении одного признака. | Notebook 1, раздел `Partial Dependence`. | scikit-learn User Guide: Partial Dependence and ICE. |
| `False Positive` | Ошибка, когда модель сказала `1`, но в реальности класс `0`. | Notebook 2, локальный разбор ошибок. | scikit-learn Guide: classification metrics. |
| `Perturbation analysis` | Локальное объяснение через замену одного признака на референсное значение и пересчет score. | Notebook 2, `error_case_explanations`. | Логика из `lab_utils.py` ЛР 02 + материалы по local explanations. |
| `Native importance` | Встроенные в модель оценки важности признаков (например, коэффициенты логистической регрессии или важности из RandomForest). Эти оценки вычисляются внутри модели и не требуют дополнительных вычислений. | ЛР 02.1, Шаг 3. Глобальные объяснения. | [scikit-learn: Feature importances](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_importances.html) |
| `Permutation importance` | Оценка важности признака через перемешивание его значений в тестовой выборке и измерение падения качества модели. Чем сильнее падает качество, тем важнее признак. | ЛР 02.1, Шаг 3. Глобальные объяснения. | [scikit-learn: Permutation Importance](https://scikit-learn.org/stable/modules/permutation_importance.html) |
| `Partial dependence` | График или таблица, показывающая, как меняется предсказание модели при изменении одного признака, усреднённого по всем остальным признакам. Помогает понять направление и форму влияния признака. | ЛР 02.1, Шаг 4. Partial Dependence. | [scikit-learn: Partial Dependence Plots](https://scikit-learn.org/stable/modules/partial_dependence.html) |
| `Local explanation` | Объяснение конкретного предсказания модели для одного объекта, показывающее, какие признаки больше всего повлияли на этот конкретный ответ. В отличие от глобального, отвечает на вопрос «почему именно этот клиент получил отказ». | ЛР 02.2, Шаг 2. Локальные объяснения ошибок. | Interpretable ML (Molnar), chapter on Local Explanations. |
| `Perturbation analysis` | Метод локального объяснения, при котором по очереди изменяют значение каждого признака (например, заменяют на среднее или нулевое) и смотрят, как меняется предсказание. Простой и модельно-независимый способ. | ЛР 02.2, `error_case_explanations`. | Логика из `lab_utils.py` ЛР 02. |
| `Segmentation` | Разбиение данных на группы (сегменты) по одному или нескольким признакам (например, возрастные группы или уровни кредитного скора). Используется для поиска системных ошибок модели в отдельных подгруппах. | ЛР 02.2, Шаг 3. Сегментный взгляд на ошибки. | [Interpretable ML (Molnar): Segmentation](https://christophm.github.io/interpretable-ml-book/) |
| `False Positive Rate` | Доля ошибок, когда модель предсказала положительный класс, а на самом деле класс отрицательный. Важная метрика для оценки системных смещений модели. | ЛР 02.2, `segment_error_summary`. | [scikit-learn: Classification metrics](https://scikit-learn.org/stable/modules/model_evaluation.html) |
| `False Negative Rate` | Доля ошибок, когда модель не заметила положительный класс. Особенно критично в задачах, где пропуск опаснее ложной тревоги (например, в медицине или кредитном скоринге). | ЛР 02.2, `segment_error_summary`. | [scikit-learn: Classification metrics](https://scikit-learn.org/stable/modules/model_evaluation.html) |