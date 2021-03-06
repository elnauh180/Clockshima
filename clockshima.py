import simpleaudio as sa
from PyQt5.QtCore import QTime, QTimer
from PyQt5.QtWidgets import QApplication, QLCDNumber


class DigitalClock(QLCDNumber):
    def __init__(self, parent=None):
        super(DigitalClock, self).__init__(parent)

        self.setSegmentStyle(QLCDNumber.Filled)
        self.setDigitCount(8)

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

        self.showTime()

        self.setWindowTitle("Clockshima")
        self.resize(280, 60)
        # self.showFullScreen()

    def showTime(self):
        time = QTime.currentTime()
        text = time.toString('hh:mm:ss')
        self.display(text)

        if time.minute() == 0:
            # show the subtitle for the respective message
            print(alarmLines[time.hour()])
            # play the appropriate file based on the time
            # wave_obj = sa.WaveObject.from_wave_file(time.hour() + '.wav')
            wave_obj = sa.WaveObject.from_wave_file(str(time.hour()) + '.wav')
            wave_obj.play()


def populateList(file):
    readIn = open(file, "r")
    lines = readIn.readlines()
    readIn.close()
    tup = tuple(lines)
    return tup


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    alarmLines = populateList('script.txt')
    clock = DigitalClock()
    clock.setStyleSheet("background-color:lightgray;");
    clock.show()
    sys.exit(app.exec_())
