import operator
import string

str_ = '“Well!” thought Alice to herself, “\
after such a fall as this, I shall think nothing of tumbling down stairs! How brave they’ll all think me at home! Why, I wouldn’t say anything' \
       ' about it, even if I fell off the top of the house!” (Which was very likely true.) Down, down, down. Would the fall never come to an end? “I wonder how many miles I’ve fallen by this time?” she said aloud. “I must be getting somewhere near the centre of the earth. Let me see: that would be four thousand miles down, I think—” (for, you see, Alice had learnt several things of this sort in her lessons in the schoolroom, and though this was not a very good opportunity for showing off her knowledge, as there was no one to listen to her, still it was good practice to say it over) “—yes, that’s about the right distance—but then I wonder what Latitude or Longitude I’ve got to?” (Alice had no idea what Latitude was, or Longitude either, but thought they were nice grand words to say.)\
Presently she began again. “I wonder if I shall fall right through the earth! How funny it’ll seem to come out among the people that walk with their heads downward! The Antipathies, I think—” (she was rather glad there was no one listening, this time, as it didn’t sound at all the right word) “—but I shall have to ask them what the name of the country is, you know. Please, Ma’am, is this New Zealand or Australia?” (and she tried to curtsey as she spoke—fancy curtseying as you’re falling through the air! Do you think you could manage it?) “And what an ignorant little girl she’ll think me for asking! No, it’ll never do to ask: perhaps I shall see it written up somewhere.”'

b = str_.split()


def clean_text(words_list):
    result = []
    for word in words_list:
        new_word = ''
        has_punch_mark = False
        for ch in string.punctuation:
            if ch in word:
                has_punch_mark = True
                pos = word.find(ch)
                if pos == len(word) - 1:
                    new_word = word[:pos]
                else:
                    new_word = word[:pos] + word[pos + 1:]
        if not has_punch_mark:
               new_word = word
               result.append(new_word.lower())
    return result
a = clean_text(b)
def count_words(words):
       words_set = set(words)
       words_dict = {}
       for word in words_set:
              words_dict[word] = words.count(word)
       return words_dict

c = sorted(count_words(a).items(), key=lambda x : x[1], reverse=True)
d = list(c)[:10]
for word, num in d:
    print(word, ': ', num)