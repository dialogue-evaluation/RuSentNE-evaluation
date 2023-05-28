# RuSentNE-2023: Соревнование по анализу тональности к именованным сущностям в новостных текстах
[![](https://img.shields.io/badge/telegram-blue?logo=telegram)](https://t.me/rusentne2023)

> :bell: **28 мая 2023:** соревнования открыты для участия в [Post-evaluation этапа](https://codalab.lisn.upsaclay.fr/competitions/9538#results)

> :book: **26 мая 2023:** результаты и итоги основного (`final`) этапа сформированы в статью

> :exclamation: **26 февраля 2023:** все обновления касательно дат фаз тестирования в первую очередь появляются в [Telegram канале соревнований](https://t.me/rusentne2023).

### [Ссылка на соревнования в системе Codalab](https://codalab.lisn.upsaclay.fr/competitions/9538)
### [:alarm_clock: Даты и график проведения соревнования](https://codalab.lisn.upsaclay.fr/competitions/9538#learn_the_details-terms_and_conditions)
### [:chart_with_upwards_trend:  Таблица результатов](https://codalab.lisn.upsaclay.fr/competitions/9538#results)
### [:newspaper: Telegram канал соревнований](https://t.me/rusentne2023)

## Описание:

Анализ тональности текста — извлечение выраженной в тексте эмоциональной оценки к некоторой сущности — одно из наиболее активно развивающихся направлений в автоматической обработке текстов. 

Анализ тональности новостных текстов — важное направление в области анализа мнений, поскольку обнаружение, отслеживание трендов тональности в новостном потоке важно для построения разного рода аналитических систем, отслеживания имиджа в СМИ конкретных людей или компаний. 

## Тональность по отношению к сущности в новостном тексте может происходить по крайней мере из трёх разных источников:
* мнения автора текста,
* цитируемого мнения, при этом сам носитель мнения может быть упомянут или не упомянут в тексте,
* имплицитного мнения, которое следует из каких-либо упомянутых действий или реакций, например, X уволил Y. Такая информация часто присутствует даже при внешне нейтральном изложении событий.
    
Участникам предлагается задача извлечения из новостных текстов тональности трёх классов (негативная, позитивная, нейтральная) по отношению к заранее размеченным сущностям типа PERSON, ORGANIZATION, PROFESSION, COUNTRY, NATIONALITY в рамках отдельного предложения.

## Базовый подход:
* `baseline_submission.zip` -- применение классификатора на основе модели [RuBERT](https://huggingface.co/DeepPavlov/rubert-base-cased) взятой в исходном состоянии.

## Описание данных:
* `sentence` - предложение
* `entity` - объект анализа тональности
* `entity_tag` - тип сущности в рамках PERSON, ORGANIZATION, PROFESSION, COUNTRY, NATIONALITY
* `label` - метка тональности (0 - нейтрально, - 1 - отрицательно, 1 - положительно)

## Организаторы:
* Лукашевич Н.В. (МГУ им. М.В. Ломоносова)
* Голубев А.А. (МГУ им. М.В. Ломоносова)
* [Русначенко Н.Л.](https://nicolay-r.github.io/) (Newcastle University)

## Источники:

[Официальная страница задачи RuSentNE на сайте Dialogue-2023](https://www.dialog-21.ru/evaluation/2023/rusentne/)

[Официальная информация по конференции Dialogue-2023](https://www.dialog-21.ru/information2023/)

[Telegram канал соревнований](https://t.me/rusentne2023)


## Ссылки

```
@inproceedings{golubev2023rusentne,
title={{RuSentNE-2023}: {E}valuating Entity-Oriented Sentiment Analysis on Russian News Texts},
author={Golubev, Anton and Rusnachenko, Nicolay and Loukachevitch, Natalia},
booktitle={Computational Linguistics and Intellectual Technologies: papers from the Annual conference ``Dialogue''},
year={2023}
}
```
