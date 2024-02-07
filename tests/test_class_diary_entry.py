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
    expected = 2
    assert actual == expected

#def test_single_function_recipe():
    # result = reading_time()
    # assert result == 'The time taken to read this is: 0:01'
    pass