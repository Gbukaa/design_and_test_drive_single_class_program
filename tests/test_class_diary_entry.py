from lib.class_diary_entry import *

def test_format_method_formats_a_diary_entry():
    diary_entry = DiaryEntry('Day One', 'Dear Diary, today I went to the shops')
    actual = diary_entry.format()
    expected = 'Day One: Dear Diary, today I went to the shops'
    assert actual == expected

def test_count_words_returns_word_count_of_diary_entry():
    diary_entry = DiaryEntry('Day One', 'Dear Diary, today I ate seven sandwiches, all filled with cheese')
    actual = diary_entry.count_words()
    expected = 11
    assert actual == expected

def test_estimated_reading_time_in_mins_at_given_wpm():
    diary_entry = DiaryEntry('Day Two', "In the bustling heart of Tokyo, neon lights painted the night sky in a kaleidoscope of colors. Amidst the towering skyscrapers and the ceaseless hum of urban life, nestled a quaint, ivy-covered teahouse. The air inside was steeped in the gentle aroma of green tea and the soothing hum of soft koto music. Inside, patrons sat on tatami mats, sipping their tea in quiet contemplation. Some were salarymen seeking respite from the days pressure, others were lost in conversation with friends, and still others were immersed in the pages of well-worn books. Each cup of tea held a silent story, a moment of peace snatched from the citys relentless rhythm. Outside, the rain began to fall, a gentle patter against the paper windows. The sound seemed to draw the patrons closer, creating a sense of shared intimacy. As the hours melted away, the teahouse became a haven, a refuge from the outside world, where time seemed to slow down and worries dissolved in the steam of a warm cup. And as they stepped back into the neon-drenched night, each person carried a piece of that serenity, a reminder of the simple beauty found in the midst of urban chaos. As the rain solidified into a steady drizzle, laughter from a nearby table wove with the koto's melody, creating a warm hum of connection. The final patrons trickled out, leaving the owner, her eyes mirroring the tea's serenity, to extinguish the lanterns.")
    actual = diary_entry.reading_time(120)
    expected = 'The time it would take to read this is 00:02:00'
    assert actual == expected

def test_single_class_init_():
    entry1 = DiaryEntry("Tuesday 6th Feb", "Don't give up.")
    result = entry1.format() 
    assert result == "Tuesday 6th Feb: Don't give up."


def test_single_class_format():
    entry2 = DiaryEntry("Wednesday 7th Feb", "There are 3 minutes more daylight every single day!")
    assert entry2.format() == "Wednesday 7th Feb: There are 3 minutes more daylight every single day!"

def test_single_class_word_count():
    entry3 = DiaryEntry ("Thursday 8th Feb", "How many words am I?")
    assert entry3.count_words() == 5


def test_single_class_reading_time():
    entry4 = DiaryEntry ("Friday 9th Feb", "This sentence should take one second!")
    assert entry4.reading_time(200) == 'The time it would take to read this is 00:00:01'

def test_single_class_reading_chunk():
    entry5 = DiaryEntry("Saturday 10th Feb", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis ac eros leo. Morbi tristique elit nec orci feugiat dignissim. Vestibulum tristique ac sapien vel tempor. Nam mattis turpis et elit pulvinar egestas. Nullam non rhoncus tortor. Fusce pellentesque facilisis ipsum. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Morbi ultrices sem metus, quis mattis ipsum convallis id. Sed porta convallis blandit. Ut imperdiet ex nec tortor blandit, pulvinar consequat purus pulvinar. Nulla arcu ex, sagittis id ornare vel, lobortis et elit. Praesent quis justo gravida, consectetur augue sed, iaculis arcu. Etiam hendrerit libero sapien, eu varius.")
    assert entry5.reading_chunk(10, 1) == "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis ac"

def test_single_class_reading_chunk_second_half():
    entry5 = DiaryEntry("Saturday 10th Feb", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis ac eros leo. Morbi tristique elit nec orci feugiat dignissim. Vestibulum tristique ac sapien vel tempor. Nam mattis turpis et elit pulvinar egestas. Nullam non rhoncus tortor. Fusce pellentesque facilisis ipsum. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Morbi ultrices sem metus, quis mattis ipsum convallis id. Sed porta convallis blandit. Ut imperdiet ex nec tortor blandit, pulvinar consequat purus pulvinar. Nulla arcu ex, sagittis id ornare vel, lobortis et elit. Praesent quis justo gravida, consectetur augue sed, iaculis arcu. Etiam hendrerit libero sapien, eu varius.")
    entry5.reading_chunk(10, 1)
    assert entry5.reading_chunk(10, 1) == "eros leo. Morbi tristique elit nec orci feugiat dignissim. Vestibulum"


    # 30 words of text: In the bustling heart of Tokyo, neon lights painted the night sky in a kaleidoscope of colors. Amidst the towering skyscrapers and the ceaseless hum of urban life, nestled a quaint