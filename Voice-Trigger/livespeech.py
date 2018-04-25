# from pocketsphinx import LiveSpeech
# from pocketsphinx import Pocketsphinx
#
# #speech = LiveSpeech()
# ps = Pocketsphinx(verbose=False)
# ps.decode()
#
# print(ps.hypothesis())

from pocketsphinx import LiveSpeech
#speech = LiveSpeech(lm=False, keyphrase='forward', kws_threshold=1e+20)
speech = LiveSpeech()
for phrase in speech:
    print(phrase.segments(detailed=True))
