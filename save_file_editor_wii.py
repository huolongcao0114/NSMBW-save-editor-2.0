from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGroupBox,
                             QLabel, QComboBox, QCheckBox, QPushButton, QSpinBox,
                             QMenuBar, QMenu, QStatusBar, QApplication, QDialog,
                            QTextBrowser, QFileDialog)
from PyQt6.QtGui import QFont, QAction, QIcon
from PyQt6.QtCore import Qt, QPoint, QDir
import os
import sys

from Save_File_Editor import SaveFileEditor
from tool import int2bool, bool2int, int_to_hex_bytes

current_dir = os.path.dirname(os.path.abspath(__file__))

class AboutDialog(QDialog):
    """制作人员与更新日志对话框"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("制作人员与更新日志")
        self.setWindowIcon(QIcon(os.path.join(current_dir, "pic.ico")))
        self.setGeometry(100, 100, 400, 500)
        self._setup_ui()
        # 如果有父窗口，则居中显示
        if parent:
            self._center_on_parent(parent)

    def _center_on_parent(self, parent):
        """将对话框居中于父窗口"""
        parent_pos = parent.mapToGlobal(QPoint(0, 0))
        parent_width = parent.width()
        parent_height = parent.height()

        x = parent_pos.x() + (parent_width - self.width()) // 2
        y = parent_pos.y() + (parent_height - self.height()) // 2

        self.move(x, y)

    def _setup_ui(self):
        """设置对话框UI"""
        layout = QVBoxLayout(self)

        # 文本浏览器 - 显示关于信息
        self.text_browser = QTextBrowser()
        self.text_browser.setOpenExternalLinks(True)  # 允许打开外部链接
        html_content = """
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
        <html><head><meta name="qrichtext" content="1" /><style type="text/css">
        p, li { white-space: pre-wrap; }
        </style></head><body style=" font-family:'SimSun'; font-size:12pt; font-weight:400; font-style:normal;">
        <p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">火龙草牌马wii存档修改器 v2.0</p>
        <p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">注意：修改器是免费的</p>
        <p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600;">第一作者：</span></p>
        <p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">打僵尸的火龙草</p>
        <p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><a href="https://space.bilibili.com/294840926"><span style=" text-decoration: underline; color:#0000ff;">https://space.bilibili.com/294840926</span></a></p>
        <p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600;">排版修正：</span></p>
        <p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">E17bits</p>
        <p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><a href="https://space.bilibili.com/179047896"><span style=" text-decoration: underline; color:#0000ff;">https://space.bilibili.com/179047896</span></a></p>
        <p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
        <p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">v0.0.1 初始版本</p>
        <p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">v0.0.2 支持读取中文目录</p>
        <p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">v0.0.3 界面重新排列</p>
        <p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">v0.0.4 修复关卡进度bug</p>
        <p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">v0.0.5 加入世界Path，位置Path，分数及已花费大金币数</p>
        <p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">v0.0.6 修复存档版本的bug以及强行生成可读取存档</p>
        <p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">v0.0.7 修复快速保存的bug以及完善生成可读取存档</p>
        <p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">v0.0.8 修复切换档位时关卡进度更新错误的bug</p>
        <p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">v0.0.9 加入快速调整关卡进度功能，界面微调</p>
        <p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">v0.0.10 加入读取临时存档的功能</p>
        <p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">v2.0 使用python与pyqt6重写了修改器</p>
        </body></html>
                """
        self.text_browser.setHtml(html_content)

        # 关闭按钮布局
        btn_layout = QHBoxLayout()
        btn_layout.addStretch()

        self.close_btn = QPushButton("关闭")
        self.close_btn.setFixedSize(80, 30)
        self.close_btn.clicked.connect(self.close)

        btn_layout.addWidget(self.close_btn)

        # 添加到主布局
        layout.addWidget(self.text_browser)
        layout.addLayout(btn_layout)

class SaveFileEditorWii(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("火龙草牌马wii存档修改器 2.0")
        self.setWindowIcon(QIcon(os.path.join(current_dir, "pic.ico")))
        self.setGeometry(100, 100, 856, 769)
        self.editor_wii = SaveFileEditor(os.path.join(current_dir, "wii.yaml"))
        self.wl = [0, 0]#用于存储关卡编号w-l
        self._setup_ui()

    def disable_all_widgets(self, enable=False):
        """递归启用/禁用所有子组件"""
        for child in self.findChildren(QWidget):
            child.setEnabled(enable)

    def _setup_ui(self):
        """设置用户界面"""
        # 设置字体
        self.setFont(QFont("微软雅黑", 10))

        # 创建主窗口部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # 主布局 - 使用三列布局
        main_layout = QHBoxLayout(central_widget)

        # 创建三列布局
        left_column = self._create_left_column()
        middle_column = self._create_middle_column()
        right_column = self._create_right_column()

        main_layout.addLayout(left_column, stretch=1)
        main_layout.addLayout(middle_column, stretch=1)
        main_layout.addLayout(right_column, stretch=1)

        #将操作部分禁用
        self.disable_all_widgets()

        # 菜单栏
        self._create_menus()

        # 状态栏
        self.statusBar().showMessage("就绪")

    def _create_left_column(self):
        """创建左侧布局"""
        layout = QVBoxLayout()
        layout.setSpacing(10)

        # 创建上下两个主要部分
        top_layout = QHBoxLayout()
        top_layout.setSpacing(10)

        # 上部左侧 - 存档相关组
        save_group = self._create_save_group()
        top_layout.addWidget(save_group)

        # 上部右侧 - 存档星星组
        star_group = self._create_star_group()
        top_layout.addWidget(star_group)

        # 下部 - 人物数据组（占据整个宽度）
        char_group = self._create_character_group()

        # 添加到主布局
        layout.addLayout(top_layout)
        layout.addWidget(char_group)
        layout.addStretch()
        return layout

    def _create_middle_column(self):
        """创建中间布局"""
        layout = QVBoxLayout()
        layout.setSpacing(10)

        # 世界解锁组
        world_group = self._create_world_group()

        # 砖块状态组
        brick_group = self._create_brick_group()

        # 分数组
        score_group = self._create_score_group()

        # 大金币数组
        star_group = self._create_unspend_star_group()

        layout.addWidget(world_group)
        layout.addWidget(brick_group)
        layout.addWidget(score_group)
        layout.addWidget(star_group)
        layout.addStretch()
        return layout

    def _create_right_column(self):
        """创建右侧布局"""
        layout = QVBoxLayout()
        layout.setSpacing(10)

        # 关卡进度调整组
        level_group = self._create_level_group()

        # 位置调整组
        pos_group = self._create_position_group()

        # 道具组
        item_group = self._create_item_group()

        layout.addWidget(level_group)
        layout.addWidget(pos_group)
        layout.addWidget(item_group)
        layout.addStretch()
        return layout

    def _create_save_group(self):
        """创建存档相关组"""
        group = QGroupBox("存档相关")
        layout = QVBoxLayout()

        # 读取档位选择
        layout.addWidget(QLabel("选择读取档位"))
        self.data_choose = QComboBox()
        self.data_choose.addItems(["存档1", "存档2", "存档3", "临时存档1", "临时存档2", "临时存档3"])
        self.data_choose.currentIndexChanged.connect(self._data_choose)
        layout.addWidget(self.data_choose)

        # 保存档位选择
        layout.addWidget(QLabel("选择保存档位"))
        self.save_choose = QComboBox()
        self.save_choose.addItems(["存档1", "存档2", "存档3", "临时存档1", "临时存档2", "临时存档3"])
        layout.addWidget(self.save_choose)

        # 自动更新文件
        self.auto_update = QCheckBox("自动更新数据")
        self.auto_update.setChecked(1)
        layout.addWidget(self.auto_update)

        # 存档版本
        layout.addWidget(QLabel("存档版本"))
        self.type_change = QComboBox()
        self.type_change.addItems(["美版", "台版", "日版", "欧版"])
        self.type_change.currentIndexChanged.connect(self._type_change)
        layout.addWidget(self.type_change)

        # 按钮
        btn_layout = QHBoxLayout()
        self.update_btn = QPushButton("更新数据")
        self.update_btn.clicked.connect(self._update_data)
        self.save_btn = QPushButton("保存存档")
        self.save_btn.clicked.connect(self._save_file)
        btn_layout.addWidget(self.update_btn)
        btn_layout.addWidget(self.save_btn)
        layout.addLayout(btn_layout)

        group.setLayout(layout)
        return group

    def _create_star_group(self):
        """创建存档星星组"""
        group = QGroupBox("存档星星")
        layout = QVBoxLayout()

        self.star_checks = []
        star_names = ["第一颗星", "第二颗星", "第三颗星", "第四颗星", "第五颗星", "闪光"]

        for name in star_names:
            checkbox = QCheckBox(name)
            self.star_checks.append(checkbox)
            layout.addWidget(checkbox)

        group.setLayout(layout)
        return group

    def _create_character_group(self):
        """创建人物数据组"""
        group = QGroupBox("人物数据")
        layout = QVBoxLayout()

        # 表头
        header_layout = QHBoxLayout()
        header_layout.addWidget(QLabel(""))  # 空白占位
        header_layout.addWidget(QLabel("命数"), alignment=Qt.AlignmentFlag.AlignCenter)
        header_layout.addWidget(QLabel("金币"), alignment=Qt.AlignmentFlag.AlignCenter)
        header_layout.addWidget(QLabel("状态"), alignment=Qt.AlignmentFlag.AlignCenter)
        header_layout.addWidget(QLabel(""))  # 空白占位
        layout.addLayout(header_layout)

        # 角色数据
        characters = [
            ("马里奥", "m"),
            ("路易吉", "l"),
            ("蓝蘑菇", "b"),
            ("黄蘑菇", "y")
        ]

        self.char_widgets = {}
        for name, prefix in characters:
            row_layout = QHBoxLayout()
            row_layout.addWidget(QLabel(name))

            # 命数
            life_spin = QSpinBox()
            life_spin.setRange(0, 255)
            life_spin.setFixedWidth(80)

            # 金币
            coin_spin = QSpinBox()
            coin_spin.setFixedWidth(80)

            # 状态
            state_combo = QComboBox()
            state_combo.addItems(["普通", "蘑菇", "火花", "迷你", "飞机", "企鹅", "冰花", "锤子"])
            state_combo.setFixedWidth(100)

            # 无敌
            invincible_check = QCheckBox("无敌")

            row_layout.addWidget(life_spin)
            row_layout.addWidget(coin_spin)
            row_layout.addWidget(state_combo)
            row_layout.addWidget(invincible_check)

            layout.addLayout(row_layout)
            self.char_widgets[prefix] = (life_spin, coin_spin, state_combo, invincible_check)

        group.setLayout(layout)
        return group

    def _create_world_group(self):
        """创建世界解锁组"""
        group = QGroupBox("世界解锁")
        layout = QVBoxLayout()

        self.world_checks = []
        for i in range(1, 11):
            checkbox = QCheckBox(f"第{i}世界")
            self.world_checks.append(checkbox)
            layout.addWidget(checkbox)

        group.setLayout(layout)
        return group

    def _create_brick_group(self):
        """创建砖块状态组"""
        group = QGroupBox("砖块状态")
        layout = QVBoxLayout()

        self.brick_checks = []
        colors = ["红", "绿", "黄", "蓝"]
        for color in colors:
            checkbox = QCheckBox(color)
            self.brick_checks.append(checkbox)
            layout.addWidget(checkbox)

        group.setLayout(layout)
        return group

    def _create_score_group(self):
        """创建分数组"""
        group = QGroupBox("分数")
        layout = QVBoxLayout()

        self.score_spin = QSpinBox()
        self.score_spin.setRange(0, 99999950)
        self.score_spin.setFixedWidth(150)
        layout.addWidget(self.score_spin, alignment=Qt.AlignmentFlag.AlignLeft)

        group.setLayout(layout)
        return group

    def _create_unspend_star_group(self):
        """创建已花费大金币数组"""
        group = QGroupBox("已花费大金币数")
        layout = QVBoxLayout()

        self.unspendstar_spin = QSpinBox()
        self.unspendstar_spin.setRange(0, 1260)
        self.unspendstar_spin.setFixedWidth(150)
        layout.addWidget(self.unspendstar_spin, alignment=Qt.AlignmentFlag.AlignLeft)

        group.setLayout(layout)
        return group

    def _create_level_group(self):
        """创建关卡进度调整组"""
        group = QGroupBox("关卡进度调整")
        layout = QVBoxLayout()

        # 关卡编号
        level_num_layout = QHBoxLayout()
        level_num_layout.addWidget(QLabel("关卡编号:"))

        self.world_spin = QSpinBox()
        self.world_spin.setRange(1, 10)
        self.world_spin.setFixedWidth(60)
        self.world_spin.valueChanged.connect(self._world_spin)

        self.level_spin = QSpinBox()
        self.level_spin.setRange(1, 42)
        self.level_spin.setFixedWidth(60)
        self.level_spin.valueChanged.connect(self._level_spin)

        level_num_layout.addWidget(self.world_spin)
        level_num_layout.addWidget(QLabel("世界"))
        level_num_layout.addWidget(self.level_spin)
        level_num_layout.addWidget(QLabel("关卡"))
        level_num_layout.addStretch()
        layout.addLayout(level_num_layout)

        # 金币收集状况
        coin_layout = QHBoxLayout()
        coin_layout.addWidget(QLabel("金币收集状况:"))

        self.starcoin_checks = []
        for i in range(1, 4):
            checkbox = QCheckBox(f"第{i}个")
            self.starcoin_checks.append(checkbox)
            coin_layout.addWidget(checkbox)
        coin_layout.addStretch()
        layout.addLayout(coin_layout)

        # 关卡解锁状况
        unlock_layout = QHBoxLayout()
        unlock_layout.addWidget(QLabel("关卡解锁状况:"))

        self.unlocked_check = QCheckBox("解锁")
        unlock_layout.addWidget(self.unlocked_check)
        unlock_layout.addStretch()
        layout.addLayout(unlock_layout)

        # 出口状态
        goal_layout = QHBoxLayout()
        goal_layout.addWidget(QLabel("出口状态:"))

        self.goal_checks = []
        goal_names = ["正常出口", "隐藏出口", "正常(红)", "隐藏(红)"]
        for name in goal_names:
            checkbox = QCheckBox(name)
            self.goal_checks.append(checkbox)
            goal_layout.addWidget(checkbox)
        goal_layout.addStretch()
        layout.addLayout(goal_layout)

        # 快速设置
        layout.addWidget(QLabel("快速进行关卡进度调整:"))

        btn_layout = QHBoxLayout()
        self.set_8_btn = QPushButton("前八个世界")
        self.set_all_btn = QPushButton("全部世界")
        self.set_8_btn.clicked.connect(self._set_8_btn)
        self.set_all_btn.clicked.connect(self._set_all_btn)
        btn_layout.addWidget(self.set_8_btn)
        btn_layout.addWidget(self.set_all_btn)
        layout.addLayout(btn_layout)

        # 世界编号设置
        world_set_layout = QHBoxLayout()
        world_set_layout.addWidget(QLabel("应用设置到世界:"))

        self.world2_spin = QSpinBox()
        self.world2_spin.setRange(1, 10)
        self.world2_spin.setFixedWidth(60)

        self.set_w_btn = QPushButton("应用")
        self.set_w_btn.clicked.connect(self._set_w_btn)
        world_set_layout.addWidget(self.world2_spin)
        world_set_layout.addWidget(self.set_w_btn)
        world_set_layout.addStretch()
        layout.addLayout(world_set_layout)

        group.setLayout(layout)
        return group

    def _create_position_group(self):
        """创建位置调整组"""
        group = QGroupBox("位置调整")
        layout = QHBoxLayout()

        # 世界路径
        world_path_layout = QVBoxLayout()
        world_path_layout.addWidget(QLabel("世界路径"))
        self.worldpath_spin = QSpinBox()
        self.worldpath_spin.setRange(0, 255)
        world_path_layout.addWidget(self.worldpath_spin)

        # 位置路径
        path_layout = QVBoxLayout()
        path_layout.addWidget(QLabel("位置路径"))
        self.path_spin = QSpinBox()
        self.path_spin.setRange(0, 255)
        path_layout.addWidget(self.path_spin)

        layout.addLayout(world_path_layout)
        layout.addLayout(path_layout)
        group.setLayout(layout)
        return group

    def _create_item_group(self):
        """创建道具组"""
        group = QGroupBox("道具")
        layout = QHBoxLayout()

        # 左侧道具列
        left_item_layout = QVBoxLayout()
        item_names = ["蘑菇", "火花", "飞机", "冰花", "企鹅", "迷你", "无敌", "锤子"]
        self.left_item_spins = []

        for name in item_names:
            item_layout = QHBoxLayout()
            item_layout.addWidget(QLabel(f"{name}:"))

            spin = QSpinBox()
            spin.setRange(0, 255)
            spin.setFixedWidth(60)
            item_layout.addWidget(spin)

            left_item_layout.addLayout(item_layout)
            self.left_item_spins.append(spin)

        # 右侧道具列
        right_item_layout = QVBoxLayout()
        item_names = [f"道具{i}" for i in range(9, 17)]
        self.right_item_spins = []

        for name in item_names:
            item_layout = QHBoxLayout()
            item_layout.addWidget(QLabel(f"{name}:"))

            spin = QSpinBox()
            spin.setRange(0, 255)
            spin.setFixedWidth(60)
            item_layout.addWidget(spin)

            right_item_layout.addLayout(item_layout)
            self.right_item_spins.append(spin)

        layout.addLayout(left_item_layout)
        layout.addLayout(right_item_layout)
        group.setLayout(layout)
        return group

    def _create_menus(self):
        """创建菜单栏"""
        menubar = self.menuBar()

        # 文件菜单
        file_menu = menubar.addMenu("文件")

        open_action = QAction("打开...", self)
        open_action.triggered.connect(self._open_file)
        open_action.setShortcut("Ctrl+O")

        self.save_action = QAction("保存", self)  # 变为实例变量
        self.save_action.triggered.connect(self._save_file)
        self.save_action.setShortcut("Ctrl+S")
        self.save_action.setEnabled(False)

        exit_action = QAction("退出", self)
        exit_action.triggered.connect(self.close)

        file_menu.addAction(open_action)
        file_menu.addAction(self.save_action)
        file_menu.addSeparator()
        file_menu.addAction(exit_action)

        # 关于菜单
        about_menu = menubar.addMenu("关于")

        author_action = QAction("制作人员与更新日志", self)
        author_action.triggered.connect(self._show_about)
        about_menu.addAction(author_action)

    def _open_file(self):
        """打开文件操作"""
        self.statusBar().showMessage("打开文件...", 3000)
        # 获取上一次打开的路径（默认为程序所在目录）
        if not hasattr(self, '_last_open_dir'):
            self._last_open_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

        # 使用静态方法打开文件对话框
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "选择存档文件",
            self._last_open_dir,  # 默认目录
            "存档文件 (*.sav);;所有文件 (*)"
        )

        if file_path:
            # 更新上一次打开的路径（保存文件所在目录）
            self._last_open_dir = os.path.dirname(file_path)
            # 显示选中的文件（自动处理中文）
            display_path = os.path.basename(file_path)
            self.statusBar().showMessage(f"已选择: {display_path}", 5000)

            # 实际处理文件
            self.disable_all_widgets(True)
            self.save_action.setEnabled(True)
            self.editor_wii.load_file(file_path)
            lst = self.editor_wii.config["save_list"] + self.editor_wii.config["quick_save_list"]
            dci = self.data_choose.currentIndex()
            self.editor_wii.set_save_index(lst[dci])
            self._init_qt_data()

    def _save_file(self):
        """保存文件操作"""
        self.statusBar().showMessage("保存文件...", 3000)
        if self.auto_update.isChecked():
            self._update_data()
        self.editor_wii.save_file()

    def _show_about(self):
        """显示关于信息"""
        self.statusBar().showMessage("关于: Save File Editor Wii版 v2.0", 3000)
        dialog = AboutDialog(self)
        dialog.exec()  # 使用exec()以模态方式显示对话框

    def _type_change(self):
        val = self.type_change.currentIndex()
        version_map = [
            'E',  # 美版
            'W',  # 台版
            'J',  # 日版
            'P'  # 欧版
        ]
        self.editor_wii.data["f_head"]["data"][3] = ord(version_map[val])

    def _data_choose(self):
        lst = self.editor_wii.config["save_list"] + self.editor_wii.config["quick_save_list"]
        dci = self.data_choose.currentIndex()
        if self.auto_update.isChecked():
            self._update_data()
        self.save_choose.setCurrentIndex(dci)
        self.editor_wii.set_save_index(lst[dci])
        self._init_qt_data()

    def _update_data(self):
        self._update_save_data()
        self._update_level_data()
        lst = self.editor_wii.config["save_list"] + self.editor_wii.config["quick_save_list"]
        self.editor_wii.update_data(lst[self.save_choose.currentIndex()])

    def _update_save_data(self):
        location = self.editor_wii.config["save_data"]
        e = self.editor_wii
        pc = location["players"]["coins"]
        pl = location["players"]["lives"]
        ps = location["players"]["star"]
        pi = location["players"]["item"]
        pp = ["m", "l", "b", "y"]
        for i in range(0, 4):
            e.set_value(self.char_widgets[pp[i]][0].value(), pl[i])
            e.set_value(self.char_widgets[pp[i]][1].value(), pc[i])
            e.set_value(self.char_widgets[pp[i]][2].currentIndex(), pi[i])
            e.set_value(self.char_widgets[pp[i]][3].isChecked(), ps[i])

        ss = []
        for i in range(0, 6):
            ss.append(self.star_checks[i].isChecked())
        [s1, s2, s3, s4, s5, s0] = ss
        e.set_value(bool2int([0, 0, s5, s4, s3, s2, s1, s0 == 0]), location["stars"])

        for i in range(0, 10):
            e.set_value(self.world_checks[i].isChecked(), location["map"][i])

        sw = []
        for i in range(0, 4):
            sw.append(self.brick_checks[i].isChecked())
        [_r, _g, _y, _b] = sw
        e.set_value(bool2int([0, 0, 0, 0, _b, _y, _g, _r]), location["switch"])

        sco = int_to_hex_bytes(self.score_spin.value())
        stc = int_to_hex_bytes(self.unspendstar_spin.value())
        for i in range(0, 4):
            e.set_value(sco[i], location["score"][i])
            e.set_value(stc[i], location["spent_coin"][i])

        e.set_value(self.worldpath_spin.value(), location["pos"][0])
        e.set_value(self.path_spin.value(), location["pos"][1])

        it = location["items"]
        for i in range(0, 8):
            e.set_value(self.left_item_spins[i].value(), it[i])
            e.set_value(self.right_item_spins[i].value(), it[i + 8])

    def _update_level_data(self):
        level = self.editor_wii.config["save_data"]["level_progress"]
        e = self.editor_wii
        pos = [val + 168 * self.wl[0] + 4 * self.wl[1] for val in level["pos"]]
        _sc = []
        for i in range(0, 3):
            _sc.append(self.starcoin_checks[i].isChecked())
        [_c1, _c2, _c3] = _sc
        _go = []
        for i in range(0, 4):
            _go.append(self.goal_checks[i].isChecked())
        [_n, _h, _sgn, _sgh] = _go
        _ul = self.unlocked_check.isChecked()
        e.set_value(bool2int([0, 0, 0, 0, 0, 0, _ul, _sgh]), pos[0])
        e.set_value(bool2int([_sgn, 0, _h, _n, 0, _c3, _c2, _c1]), pos[1])

    def _level_spin(self):
        self._update_level_data()
        self.wl[1] = self.level_spin.value() - 1
        self._init_qt_level()

    def _world_spin(self):
        self._update_level_data()
        self.wl[0] = self.world_spin.value() - 1
        self._init_qt_level()

    def _set_w_btn(self):
        pos0 = self.editor_wii.config["save_data"]["level_progress"]["pos"]
        e = self.editor_wii
        _sc = []
        for i in range(0, 3):
            _sc.append(self.starcoin_checks[i].isChecked())
        [_c1, _c2, _c3] = _sc
        _go = []
        for i in range(0, 4):
            _go.append(self.goal_checks[i].isChecked())
        [_n, _h, _sgn, _sgh] = _go
        _ul = self.unlocked_check.isChecked()
        w = self.world2_spin.value() - 1
        for l in range(0, 42):
            pos = [val + 168 * w + 4 * l for val in pos0]
            e.set_value(bool2int([0, 0, 0, 0, 0, 0, _ul, _sgh]), pos[0])
            e.set_value(bool2int([_sgn, 0, _h, _n, 0, _c3, _c2, _c1]), pos[1])

    def _set_8_btn(self):
        pos0 = self.editor_wii.config["save_data"]["level_progress"]["pos"]
        e = self.editor_wii
        _sc = []
        for i in range(0, 3):
            _sc.append(self.starcoin_checks[i].isChecked())
        [_c1, _c2, _c3] = _sc
        _go = []
        for i in range(0, 4):
            _go.append(self.goal_checks[i].isChecked())
        [_n, _h, _sgn, _sgh] = _go
        _ul = self.unlocked_check.isChecked()
        for w in range(0, 8):
            for l in range(0, 42):
                pos = [val + 168 * w + 4 * l for val in pos0]
                e.set_value(bool2int([0, 0, 0, 0, 0, 0, _ul, _sgh]), pos[0])
                e.set_value(bool2int([_sgn, 0, _h, _n, 0, _c3, _c2, _c1]), pos[1])

    def _set_all_btn(self):
        pos0 = self.editor_wii.config["save_data"]["level_progress"]["pos"]
        e = self.editor_wii
        _sc = []
        for i in range(0, 3):
            _sc.append(self.starcoin_checks[i].isChecked())
        [_c1, _c2, _c3] = _sc
        _go = []
        for i in range(0, 4):
            _go.append(self.goal_checks[i].isChecked())
        [_n, _h, _sgn, _sgh] = _go
        _ul = self.unlocked_check.isChecked()
        for w in range(0, 10):
            for l in range(0, 42):
                pos = [val + 168 * w + 4 * l for val in pos0]
                e.set_value(bool2int([0, 0, 0, 0, 0, 0, _ul, _sgh]), pos[0])
                e.set_value(bool2int([_sgn, 0, _h, _n, 0, _c3, _c2, _c1]), pos[1])


    def _init_qt_level(self):
        e = self.editor_wii
        level = e.config["save_data"]["level_progress"]
        pos = [val + 168 * self.wl[0] + 4 * self.wl[1] for val in level["pos"]]
        [_, _, _, _, _, _, _ul, _sgh] = int2bool(e.get_val(pos[0]))
        [_sgn, _, _h, _n, _, _c3, _c2, _c1] = int2bool(e.get_val(pos[1]))
        self.unlocked_check.setChecked(_ul)
        _sc = [_c1, _c2, _c3]
        for i in range(0, 3):
            self.starcoin_checks[i].setChecked(_sc[i])
        _go = [_n, _h, _sgn, _sgh]
        for i in range(0, 4):
            self.goal_checks[i].setChecked(_go[i])

    def _init_qt_data(self):
        location = self.editor_wii.config["save_data"]
        e = self.editor_wii
        version_char = self.editor_wii.data["f_head"]["data"][3]  # 获取版本字符
        version_map = {
            ord('E'): 0,  # 美版
            ord('W'): 1,  # 台版
            ord('J'): 2,  # 日版
            ord('P'): 3  # 欧版
        }
        # 设置对应的索引，如果字符不匹配则默认美版
        self.type_change.setCurrentIndex(version_map.get(version_char, 0))
        # 如果需要修改 head[3] 的默认值
        if version_char not in version_map:
            self.editor_wii.data["f_head"]["data"][3] = ord('E')  # 修改为默认值
            self.type_change.setCurrentIndex(0)  # 确保 UI 同步

        pc = location["players"]["coins"]
        pl = location["players"]["lives"]
        ps = location["players"]["star"]
        pi = location["players"]["item"]
        pp = ["m", "l", "b", "y"]
        for i in range(0,4):
            self.char_widgets[pp[i]][0].setValue(e.get_val(pl[i]))
            self.char_widgets[pp[i]][1].setValue(e.get_val(pc[i]))
            self.char_widgets[pp[i]][2].setCurrentIndex(e.get_val(pi[i]))
            self.char_widgets[pp[i]][3].setChecked(e.get_val(ps[i]))

        [_, _, s5, s4, s3, s2, s1, s0] = int2bool(e.get_val(location["stars"]))
        ss = [s1, s2, s3, s4, s5, s0==0]
        for i in range(0, 6):
            self.star_checks[i].setChecked(ss[i])

        for i in range(0, 10):
            self.world_checks[i].setChecked(e.get_val(location["map"][i]))

        [_, _, _, _, _b, _y, _g, _r] = int2bool(e.get_val(location["switch"]))
        sw = [_r, _g, _y, _b]
        for i in range(0, 4):
            self.brick_checks[i].setChecked(sw[i])

        sco = 0
        stc = 0
        for i in range(0, 4):
            sco = e.get_val(location["score"][i]) + 256 * sco
            stc = e.get_val(location["spent_coin"][i]) + 256 * stc
        self.score_spin.setValue(sco)
        self.unspendstar_spin.setValue(stc)

        self.worldpath_spin.setValue(e.get_val(location["pos"][0]))
        self.path_spin.setValue(e.get_val(location["pos"][1]))

        it = location["items"]
        for i in range(0, 8):
            self.left_item_spins[i].setValue(e.get_val(it[i]))
            self.right_item_spins[i].setValue(e.get_val(it[i + 8]))

        self._init_qt_level()




if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 设置应用程序样式
    app.setStyle("Fusion")

    app.setWindowIcon(QIcon(os.path.join(current_dir, "pic.ico")))   # 应用程序全局图标（任务栏）

    window = SaveFileEditorWii()
    window.show()

    sys.exit(app.exec())