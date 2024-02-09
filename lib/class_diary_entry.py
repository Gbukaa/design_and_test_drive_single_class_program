from datetime import timedelta

class DiaryEntry:
    def __init__(self, title, contents):
        if title == "" or contents == "":
            raise Exception('Diary entries must have a title or contents')
        self.title = title
        self.contents = contents
        self.words_read = 0 
        # Parameters:
        #   title: string
        #   contents: string

    def format(self):
            return f"{self.title}: {self.contents}"

        # Returns:
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"

    def count_words(self):
        words = self.contents.split()
        word_count = len(words)
        return word_count
        #wants to count individual words in string, separated by ' '. returns the count.
        # Returns:
        #   int: the number of words in the diary entry
        pass

    def reading_time(self, wpm):
        self.contents = self.contents.split()
        mins = len(self.contents) / wpm
        time_delta = timedelta(minutes = mins)
        hours = time_delta.seconds // 3600
        minutes = (time_delta.seconds % 3600) // 60
        seconds = time_delta.seconds % 60
        time_spent_reading = f'The time it would take to read this is {hours:02d}:{minutes:02d}:{seconds:02d}'
        return time_spent_reading


        
        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.
        pass

    def reading_chunk(self, wpm, minutes):
        self.contents = self.contents.split()
        words_readable = minutes * wpm
        string_to_read = self.contents[self.words_read: self.words_read + words_readable]
        self.contents = ' '.join(self.contents)
        self.words_read = self.words_read + words_readable
        if self.words_read >= len(self.contents):
            self.words_read = 0
        return ' '.join(string_to_read)



        
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        pass

#More complex code for chunk - to complex for now!
#  def reading_chunk(self, wpm, minutes):
#         if wpm < 0 or minutes < 0:
#             raise ValueError('wpm and minutes must be non-negative')
        
#         self.read_words = getattr(self, "read_words", 0)
#         words_to_read = min(wpm * minutes, self.count_words() - self.read_words)
#         if words_to_read == 0:
#             self.read_words = 0
#             return ""
        
#         start_index = self.read_words
#         end_index = start_index + words_to_read
#         while end_index >0 and not self.contents[end_index -1].isspace():
#             end_index -= 1
        
#         self.read_words = end_index

#         chunk = self.contents[start_index:end_index]
#         if self.read_words == 0:
#             formatted_chunk = f"{self.title:} {self.format(chunk)}"
#         else:
#             formatted_chunk = self.format(chunk)
#         return formatted_chunk