# 工厂方法模式（Factory Method）- 文档编辑器

## 模式原理

### 意图
define一个用于创建对象的接口，让子类决定实例化哪一个类。Factory Method使一个类的实例化延迟到其子类。

### 适用场景
- 当一个类不知道它所必须创建的对象的类的时候
- 当一个类希望由它的子类来指定它所创建的对象的时候
- 当类将创建对象的职责委托给多个帮助子类中的某一个，并且你希望将哪一个帮助子类是代理者这一信息局部化的时候

### 关键参与者
- **Product（产品）**：定义工厂方法所创建的对象的接口
- **ConcreteProduct（具体产品）**：实现Product接口
- **Creator（创建者）**：声明工厂方法，该方法返回一个Product类型的对象；可以调用工厂方法创建一个Product对象
- **ConcreteCreator（具体创建者）**：重定义工厂方法以返回一个ConcreteProduct实例

## 示例故事

本示例采用"文档编辑器"场景：
- 不同的应用程序（Word、Excel）创建不同类型的文档
- 应用程序基类定义工厂方法，子类决定具体创建哪种文档

对应关系：
- `Document` → Product（产品接口）
- `WordDocument`、`ExcelDocument` → ConcreteProduct（具体产品）
- `Application` → Creator（创建者）
- `WordApplication`、`ExcelApplication` → ConcreteCreator（具体创建者）

## 运行说明

### 环境要求
- Python 3.10+

### 运行方式
```bash
python document_editor.py
```

### 预期输出
```
=== Word 应用程序 ===
创建 Word 文档
打开文档: 年度报告.docx
Word 文档内容: [Word 文档内容]
保存文档
=== Excel 应用程序 ===
创建 Excel 文档
打开文档: 销售数据.xlsx
Excel 文档内容: [Excel 表格数据]
保存文档
```

## 运行截图
![运行截图](screenshot.png)
