import pymysql
from pyecharts.charts import Line
from pyecharts import options as opts
from pyecharts.charts import Bar, Pie, Page
from pyecharts.globals import ThemeType

db = pymysql.connect(user="root", passwd="zak@123456", db="monitor", host="1.117.176.78")
cur1 = db.cursor()
cur2 = db.cursor()
cur3 = db.cursor()

SQL1="""SELECT TIME,cpu,mem_percent FROM system_info WHERE TIME > DATE_SUB(NOW(), INTERVAL 60 MINUTE)"""  #查询最近1h内数据展示

SQL2 = 'select disk1,disk2 from system_info order by TIME desc limit 1'

SQL3 = 'select mem_free,mem_total,mem_percent,mem_used from system_info order by TIME desc limit 1'

cur1.execute(SQL1)
cur2.execute(SQL2)
cur3.execute(SQL3)
cpu_data = cur1.fetchall()
disk_data = cur2.fetchall()
mem_data = cur3.fetchall()

all_time = []
all_cpu = []
all_mem_percent = []
for time_cpu in cpu_data:
    TIME=time_cpu[0]
    cpu0=time_cpu[1].split('%')
    cpu_num = eval(cpu0[0])

    mem0=time_cpu[2].split('%')
    mem_percent = eval(mem0[0])

    all_cpu.append(cpu_num)
    all_time.append(TIME)
    all_mem_percent.append(mem_percent)

disk_list = list(disk_data[0])
disk_percent=[eval(x.split("%")[0]) for x in disk_list]

def tab0(name, color):  # 标题
    c = (Pie().
        set_global_opts(
        title_opts=opts.TitleOpts(title=name, pos_left='center', pos_top='center',
                                  title_textstyle_opts=opts.TextStyleOpts(color=color, font_size=20))))
    return c

def tab1(name, color):  # 标题
    c = (Pie().
        set_global_opts(
        title_opts=opts.TitleOpts(title=name, pos_left='center', pos_top='center',
                                  title_textstyle_opts=opts.TextStyleOpts(color=color, font_size=30))))
    return c

def tab2(name, color):
    c = (Pie().
        set_global_opts(
        title_opts=opts.TitleOpts(title=name, pos_left='center', pos_top='center',
                                  title_textstyle_opts=opts.TextStyleOpts(color=color, font_size=25))))
    return c

def line(all_time, all_cpu):
    line = (
        Line()
        .add_xaxis(all_time)
        .add_yaxis("CPU_info：%", all_cpu)
        .set_global_opts(title_opts=opts.TitleOpts(title="CPU_info"))
    )
    line.render()

    return line

def line1(all_time, all_mem_percent):
    line = (
        Line()
        .add_xaxis(all_time)
        .add_yaxis("Mem_percent：%",all_mem_percent)
        .set_global_opts(title_opts=opts.TitleOpts(title="内存使用占比"))
    )
    line.render()

    return line

def bar(disk_percent):

    bar =(Bar(init_opts=opts.InitOpts(theme=ThemeType.CHALK))  #在这里输入啊，设置绘图主题为CHALK
        .add_xaxis(["C盘","D盘"])
        .add_yaxis("磁盘使用占比：%",disk_percent))
    bar.render()
    return bar


def pie_base():
    c = (
        Pie()
        .add("", [list(z) for z in zip(['mem_free', 'mem_used'],
                                       [mem_data[0][0],mem_data[0][3]])])
        .set_global_opts(title_opts=opts.TitleOpts(title="内存使用占比"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    return c
#将上面图拼接到网页上
page = Page()
page.add(
    tab0("Python数据分析实例", "#2CB34A"),
    line(all_time,all_cpu),
    tab1("系统信息监控数据可视化大屏", "#2CB34A"),
    tab2("可用内存:{mem_free}\n\n总内存:{mem_total}\n\n内存占比:{mem_percent}\n\n占用内存:{mem_used}".format(mem_free=mem_data[0][0],mem_total=mem_data[0][1],mem_percent=mem_data[0][2],mem_used=mem_data[0][3]), "#000000"),
    bar(disk_percent),
    pie_base(),
    line1(all_time,all_mem_percent)
)
page.render("data_center.html")
db.close()