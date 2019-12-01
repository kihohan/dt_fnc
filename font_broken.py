import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
path = "/usr/share/fonts/truetype/nanum/NanumGothicBold.ttf"
font_name = fm.FontProperties(fname=path, size=50).get_name()
# print(font_name)
plt.rc('font', family=font_name)
