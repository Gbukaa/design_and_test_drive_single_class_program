from lib.class_diary_entry import *

def test_format_method_formats_a_diary_entry():
    diary_entry = DiaryEntry('Day One', 'Dear Diary, today I went to the shops')
    actual = diary_entry.format()
    expected = 'Day One: Dear Diary, today I went to the shops'
    assert actual == expected