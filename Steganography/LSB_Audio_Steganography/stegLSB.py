import struct
import wave as W


class StegFile:

    def __init__(self, outFile, paramTuple):
        self.file = W.open(outFile, 'wb')

        #       Setting file parameters
        self.file.setparams(paramTuple)

    def writeFile(self, numFrames, hid):
        print(numFrames)
        for byte in range(0, numFrames):
            #           1 frame = 4 bytes; pack ord data to hex and write byte by byte
            pack = struct.pack('h', hid[byte])
            self.file.writeframes(pack[:1])

    def closeStegFile(self):
        self.file.close()


class AudioFile:

    def __init__(self, inFile):
        self.file = W.open(inFile, 'rb')

    def getNumFrames(self):
        return self.file.getnframes()

    def getData(self):
        return self.file.readframes(self.getNumFrames())

    def getParamTuple(self):
        return self.file.getparams()

    def closeAudioFile(self):
        self.file.close()


class StegMsg:

    def __init__(self):
        self.msg = raw_input("Enter Message: ")

    def msgLen(self):
        return len(self.msg)
