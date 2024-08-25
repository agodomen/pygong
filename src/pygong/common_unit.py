from pint import UnitRegistry


class PintUnit:
    """
    基于pint的工具封装
    """

    ureg = UnitRegistry(preprocessors=[lambda x: x.replace("%", " percent ")])
    # 定义一些中文的前缀
    百 = ureg.define("百 = 1e2")
    千 = ureg.define("千 = 1e3")
    万 = ureg.define("万 = 1e4")
    十万 = ureg.define("十万 = 1e5")
    百万 = ureg.define("百万 = 1e6")
    亿 = ureg.define("亿 = 1e8")
    ureg.define("percent = 0.01 count = %")
    @classmethod
    def get_unit_value(cls,value):
        try:
            return cls.ureg.parse_expression(value).to(cls.ureg.dimensionless).magnitude
        except AttributeError as error:
            return cls.ureg.parse_expression(value)
    @classmethod
    def sample(cls):
        cls.ureg.define('mpg = 1 * mile / gallon')
        # 解析一个字符串
        x=cls.ureg.parse_expression("1e4 万")
        print(x.to(cls.ureg.dimensionless).magnitude)
        print(x.magnitude)
        # 假设字符串为"3.5十万米"
        x = cls.ureg.parse_expression("3.5十万")
        print(x) # 打印解析后的数量


pint_unit = PintUnit()