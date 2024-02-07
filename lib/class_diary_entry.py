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
        #return self.words.count()?
        # Returns:
        #   int: the number of words in the diary entry
        pass

    def reading_time(self, wpm):
        
        
        #maybe needs the timedelta thing here to estimate reading time - find the code we did before on this!
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
