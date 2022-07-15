# 类的基础知识点
class Dog:
    leg_num = 4

    def friend(self):
        print('狗喜欢和人类做朋友')


hsq = Dog()  # 实例化对象，并传入体重和身高值
print(hsq.leg_num)  # 打印腿的数目
hsq.friend()  # 调用方法，这里方法的内容就是打印一句话

# 进阶知识点1：self
class Dog:
    leg_num = 4

    def leg(self):
        print('狗腿数量为：' + str(self.leg_num))


hsq = Dog()
hsq.leg()
Dog.leg(hsq)  # 等同于hsq.leg()


# 进阶知识点2：初始化方法
class Dog:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height
        self.leg_num = 4


hsq = Dog(10, 50)  # 实例化对象，并传入体重和身高值
print(hsq.leg_num)  # 打印腿的数目
print(hsq.weight)  # 打印体重
print(hsq.height)  # 打印身高


