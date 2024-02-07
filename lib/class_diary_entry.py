class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        # Parameters:
        #   title: string
        #   contents: string

    def format(self):
        return f'{self.title}: {self.contents}'
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
        word_count = self.count_words()
        time_to_read = int(word_count / wpm)
        return time_to_read
        
        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.
        pass

    def reading_chunk(self, wpm, minutes):
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
