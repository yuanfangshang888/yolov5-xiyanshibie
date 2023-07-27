# 导入pyttsx3库
import pyttsx3

class Voice():
      def __init__(self):
            self.engine = pyttsx3.init()  # 创建engine并初始化
            self.engine.setProperty('rate', 150)
            self.engine.setProperty('volume', 1.0)  # 在0到1之间重设音量

      def synthesis(self, text, filename):
            self.engine.save_to_file(text, filename)
            self.engine.runAndWait()

      def play(self, filename):
            self.engine.say(filename)
            self.engine.runAndWait()
            self.engine.stop()


if __name__ == "__main__":
      speech = Voice()
      speech.synthesis('注意，请勿吸烟！', '请勿吸烟.mp3') #此句是在当前文件目录下生成mp3文件，
                                                         #语音内容就是：注意，请勿吸烟！
      speech.play('注意，请勿吸烟') #此句是直接合成语音并播放
