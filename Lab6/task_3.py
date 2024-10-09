#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# GNU Radio version: 3.10.9.2

from PyQt5 import Qt
from gnuradio import qtgui
from PyQt5 import QtCore
from gnuradio import analog
from gnuradio import blocks
import pmt
from gnuradio import digital
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import sip



class task_3(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "task_3")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.variable_constellation_0 = variable_constellation_0 = digital.constellation_calcdist([-1-1j, -1+1j, 1-1j, 1+1j], [0, 1, 2, 3],
        4, 1, digital.constellation.AMPLITUDE_NORMALIZATION).base()
        self.variable_constellation_0.set_npwr(1.0)
        self.sps = sps = 8
        self.samp_rate = samp_rate = 20000
        self.num = num = 3
        self.delay = delay = 0
        self.alpha = alpha = 1

        ##################################################
        # Blocks
        ##################################################

        self.tab = Qt.QTabWidget()
        self.tab_widget_0 = Qt.QWidget()
        self.tab_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_0)
        self.tab_grid_layout_0 = Qt.QGridLayout()
        self.tab_layout_0.addLayout(self.tab_grid_layout_0)
        self.tab.addTab(self.tab_widget_0, 'chunks_symb_t')
        self.tab_widget_1 = Qt.QWidget()
        self.tab_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_1)
        self.tab_grid_layout_1 = Qt.QGridLayout()
        self.tab_layout_1.addLayout(self.tab_grid_layout_1)
        self.tab.addTab(self.tab_widget_1, 'chunks_symb_f')
        self.tab_widget_2 = Qt.QWidget()
        self.tab_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_2)
        self.tab_grid_layout_2 = Qt.QGridLayout()
        self.tab_layout_2.addLayout(self.tab_grid_layout_2)
        self.tab.addTab(self.tab_widget_2, 'rrc_in')
        self.tab_widget_3 = Qt.QWidget()
        self.tab_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_3)
        self.tab_grid_layout_3 = Qt.QGridLayout()
        self.tab_layout_3.addLayout(self.tab_grid_layout_3)
        self.tab.addTab(self.tab_widget_3, 'rrc_out')
        self.tab_widget_4 = Qt.QWidget()
        self.tab_layout_4 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_4)
        self.tab_grid_layout_4 = Qt.QGridLayout()
        self.tab_layout_4.addLayout(self.tab_grid_layout_4)
        self.tab.addTab(self.tab_widget_4, 'passband')
        self.tab_widget_5 = Qt.QWidget()
        self.tab_layout_5 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_5)
        self.tab_grid_layout_5 = Qt.QGridLayout()
        self.tab_layout_5.addLayout(self.tab_grid_layout_5)
        self.tab.addTab(self.tab_widget_5, 'lpf_in')
        self.tab_widget_6 = Qt.QWidget()
        self.tab_layout_6 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_6)
        self.tab_grid_layout_6 = Qt.QGridLayout()
        self.tab_layout_6.addLayout(self.tab_grid_layout_6)
        self.tab.addTab(self.tab_widget_6, 'lpf_out')
        self.tab_widget_7 = Qt.QWidget()
        self.tab_layout_7 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_7)
        self.tab_grid_layout_7 = Qt.QGridLayout()
        self.tab_layout_7.addLayout(self.tab_grid_layout_7)
        self.tab.addTab(self.tab_widget_7, 'matched_out')
        self.tab_widget_8 = Qt.QWidget()
        self.tab_layout_8 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_8)
        self.tab_grid_layout_8 = Qt.QGridLayout()
        self.tab_layout_8.addLayout(self.tab_grid_layout_8)
        self.tab.addTab(self.tab_widget_8, 'delay_eyes')
        self.tab_widget_9 = Qt.QWidget()
        self.tab_layout_9 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_9)
        self.tab_grid_layout_9 = Qt.QGridLayout()
        self.tab_layout_9.addLayout(self.tab_grid_layout_9)
        self.tab.addTab(self.tab_widget_9, 'thresh_real')
        self.tab_widget_10 = Qt.QWidget()
        self.tab_layout_10 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_10)
        self.tab_grid_layout_10 = Qt.QGridLayout()
        self.tab_layout_10.addLayout(self.tab_grid_layout_10)
        self.tab.addTab(self.tab_widget_10, 'thresh_imag')
        self.tab_widget_11 = Qt.QWidget()
        self.tab_layout_11 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_11)
        self.tab_grid_layout_11 = Qt.QGridLayout()
        self.tab_layout_11.addLayout(self.tab_grid_layout_11)
        self.tab.addTab(self.tab_widget_11, 'Tab 11')
        self.tab_widget_12 = Qt.QWidget()
        self.tab_layout_12 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_12)
        self.tab_grid_layout_12 = Qt.QGridLayout()
        self.tab_layout_12.addLayout(self.tab_grid_layout_12)
        self.tab.addTab(self.tab_widget_12, 'Tab 12')
        self.top_layout.addWidget(self.tab)
        self._delay_range = qtgui.Range(0, 10, 1, 0, 200)
        self._delay_win = qtgui.RangeWidget(self._delay_range, self.set_delay, "Delay", "counter_slider", int, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._delay_win)
        self._alpha_range = qtgui.Range(0, 1, 0.1, 1, 200)
        self._alpha_win = qtgui.RangeWidget(self._alpha_range, self.set_alpha, "'alpha'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._alpha_win)
        self.root_raised_cosine_filter_0_0_0 = filter.fir_filter_fff(
            1,
            firdes.root_raised_cosine(
                3,
                80000,
                10000,
                alpha,
                88))
        self.root_raised_cosine_filter_0_0 = filter.fir_filter_fff(
            1,
            firdes.root_raised_cosine(
                3,
                80000,
                10000,
                alpha,
                88))
        self.root_raised_cosine_filter_0 = filter.fir_filter_ccf(
            1,
            firdes.root_raised_cosine(
                3,
                80000,
                10000,
                alpha,
                (11*8)))
        self.rational_resampler_xxx_1_0 = filter.rational_resampler_fff(
                interpolation=1,
                decimation=5,
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_1 = filter.rational_resampler_fff(
                interpolation=1,
                decimation=5,
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=5,
                decimation=1,
                taps=[],
                fractional_bw=0)
        self.qtgui_time_sink_x_3_2_1_0 = qtgui.time_sink_f(
            1024, #size
            samp_rate/2, #samp_rate
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_3_2_1_0.set_update_time(0.10)
        self.qtgui_time_sink_x_3_2_1_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_3_2_1_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_3_2_1_0.enable_tags(True)
        self.qtgui_time_sink_x_3_2_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_3_2_1_0.enable_autoscale(False)
        self.qtgui_time_sink_x_3_2_1_0.enable_grid(False)
        self.qtgui_time_sink_x_3_2_1_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_3_2_1_0.enable_control_panel(False)
        self.qtgui_time_sink_x_3_2_1_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_3_2_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_3_2_1_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_3_2_1_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_3_2_1_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_3_2_1_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_3_2_1_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_3_2_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_3_2_1_0_win = sip.wrapinstance(self.qtgui_time_sink_x_3_2_1_0.qwidget(), Qt.QWidget)
        self.tab_layout_9.addWidget(self._qtgui_time_sink_x_3_2_1_0_win)
        self.qtgui_time_sink_x_3_2_1 = qtgui.time_sink_f(
            1024, #size
            samp_rate/2, #samp_rate
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_3_2_1.set_update_time(0.10)
        self.qtgui_time_sink_x_3_2_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_3_2_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_3_2_1.enable_tags(True)
        self.qtgui_time_sink_x_3_2_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_3_2_1.enable_autoscale(False)
        self.qtgui_time_sink_x_3_2_1.enable_grid(False)
        self.qtgui_time_sink_x_3_2_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_3_2_1.enable_control_panel(False)
        self.qtgui_time_sink_x_3_2_1.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_3_2_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_3_2_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_3_2_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_3_2_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_3_2_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_3_2_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_3_2_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_3_2_1_win = sip.wrapinstance(self.qtgui_time_sink_x_3_2_1.qwidget(), Qt.QWidget)
        self.tab_layout_9.addWidget(self._qtgui_time_sink_x_3_2_1_win)
        self.qtgui_time_sink_x_3_2_0 = qtgui.time_sink_f(
            1024, #size
            samp_rate/2, #samp_rate
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_3_2_0.set_update_time(0.10)
        self.qtgui_time_sink_x_3_2_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_3_2_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_3_2_0.enable_tags(True)
        self.qtgui_time_sink_x_3_2_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_3_2_0.enable_autoscale(False)
        self.qtgui_time_sink_x_3_2_0.enable_grid(False)
        self.qtgui_time_sink_x_3_2_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_3_2_0.enable_control_panel(False)
        self.qtgui_time_sink_x_3_2_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_3_2_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_3_2_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_3_2_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_3_2_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_3_2_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_3_2_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_3_2_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_3_2_0_win = sip.wrapinstance(self.qtgui_time_sink_x_3_2_0.qwidget(), Qt.QWidget)
        self.tab_layout_10.addWidget(self._qtgui_time_sink_x_3_2_0_win)
        self.qtgui_time_sink_x_3_2 = qtgui.time_sink_f(
            1024, #size
            samp_rate/2, #samp_rate
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_3_2.set_update_time(0.10)
        self.qtgui_time_sink_x_3_2.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_3_2.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_3_2.enable_tags(True)
        self.qtgui_time_sink_x_3_2.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_3_2.enable_autoscale(False)
        self.qtgui_time_sink_x_3_2.enable_grid(False)
        self.qtgui_time_sink_x_3_2.enable_axis_labels(True)
        self.qtgui_time_sink_x_3_2.enable_control_panel(False)
        self.qtgui_time_sink_x_3_2.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_3_2.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_3_2.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_3_2.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_3_2.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_3_2.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_3_2.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_3_2.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_3_2_win = sip.wrapinstance(self.qtgui_time_sink_x_3_2.qwidget(), Qt.QWidget)
        self.tab_layout_9.addWidget(self._qtgui_time_sink_x_3_2_win)
        self.qtgui_time_sink_x_2 = qtgui.time_sink_c(
            1024, #size
            samp_rate, #samp_rate
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_2.set_update_time(0.10)
        self.qtgui_time_sink_x_2.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_2.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_2.enable_tags(True)
        self.qtgui_time_sink_x_2.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_2.enable_autoscale(False)
        self.qtgui_time_sink_x_2.enable_grid(False)
        self.qtgui_time_sink_x_2.enable_axis_labels(True)
        self.qtgui_time_sink_x_2.enable_control_panel(False)
        self.qtgui_time_sink_x_2.enable_stem_plot(True)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(2):
            if len(labels[i]) == 0:
                if (i % 2 == 0):
                    self.qtgui_time_sink_x_2.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_2.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_2.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_2.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_2.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_2.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_2.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_2.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_2_win = sip.wrapinstance(self.qtgui_time_sink_x_2.qwidget(), Qt.QWidget)
        self.tab_layout_3.addWidget(self._qtgui_time_sink_x_2_win)
        self.qtgui_time_sink_x_1 = qtgui.time_sink_c(
            1024, #size
            samp_rate, #samp_rate
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1.enable_tags(True)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1.enable_autoscale(False)
        self.qtgui_time_sink_x_1.enable_grid(False)
        self.qtgui_time_sink_x_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_1.enable_control_panel(False)
        self.qtgui_time_sink_x_1.enable_stem_plot(True)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(2):
            if len(labels[i]) == 0:
                if (i % 2 == 0):
                    self.qtgui_time_sink_x_1.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_1.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1.qwidget(), Qt.QWidget)
        self.tab_layout_1.addWidget(self._qtgui_time_sink_x_1_win)
        self.qtgui_time_sink_x_0_0_1_0_0_1_1_0 = qtgui.time_sink_f(
            1024, #size
            10000, #samp_rate
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0_0_1_0_0_1_1_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_1_0_0_1_1_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0_1_0_0_1_1_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_1_0_0_1_1_0.enable_tags(True)
        self.qtgui_time_sink_x_0_0_1_0_0_1_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_1_0_0_1_1_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_1_0_0_1_1_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_1_0_0_1_1_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_1_0_0_1_1_0.enable_control_panel(True)
        self.qtgui_time_sink_x_0_0_1_0_0_1_1_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_1_0_0_1_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_1_0_0_1_1_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_1_0_0_1_1_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_1_0_0_1_1_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_1_0_0_1_1_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_1_0_0_1_1_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_1_0_0_1_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_1_0_0_1_1_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_1_0_0_1_1_0.qwidget(), Qt.QWidget)
        self.tab_layout_7.addWidget(self._qtgui_time_sink_x_0_0_1_0_0_1_1_0_win)
        self.qtgui_time_sink_x_0_0_1_0_0_1_1 = qtgui.time_sink_f(
            1024, #size
            10000, #samp_rate
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0_0_1_0_0_1_1.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_1_0_0_1_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0_1_0_0_1_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_1_0_0_1_1.enable_tags(True)
        self.qtgui_time_sink_x_0_0_1_0_0_1_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_1_0_0_1_1.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_1_0_0_1_1.enable_grid(False)
        self.qtgui_time_sink_x_0_0_1_0_0_1_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_1_0_0_1_1.enable_control_panel(True)
        self.qtgui_time_sink_x_0_0_1_0_0_1_1.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_1_0_0_1_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_1_0_0_1_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_1_0_0_1_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_1_0_0_1_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_1_0_0_1_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_1_0_0_1_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_1_0_0_1_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_1_0_0_1_1_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_1_0_0_1_1.qwidget(), Qt.QWidget)
        self.tab_layout_7.addWidget(self._qtgui_time_sink_x_0_0_1_0_0_1_1_win)
        self.qtgui_freq_sink_x_6 = qtgui.freq_sink_f(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_6.set_update_time(0.10)
        self.qtgui_freq_sink_x_6.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_6.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_6.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_6.enable_autoscale(False)
        self.qtgui_freq_sink_x_6.enable_grid(False)
        self.qtgui_freq_sink_x_6.set_fft_average(1.0)
        self.qtgui_freq_sink_x_6.enable_axis_labels(True)
        self.qtgui_freq_sink_x_6.enable_control_panel(False)
        self.qtgui_freq_sink_x_6.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_6.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_6.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_6.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_6.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_6.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_6.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_6_win = sip.wrapinstance(self.qtgui_freq_sink_x_6.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_6_win)
        self.qtgui_freq_sink_x_4 = qtgui.freq_sink_f(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_4.set_update_time(0.10)
        self.qtgui_freq_sink_x_4.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_4.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_4.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_4.enable_autoscale(False)
        self.qtgui_freq_sink_x_4.enable_grid(False)
        self.qtgui_freq_sink_x_4.set_fft_average(1.0)
        self.qtgui_freq_sink_x_4.enable_axis_labels(True)
        self.qtgui_freq_sink_x_4.enable_control_panel(False)
        self.qtgui_freq_sink_x_4.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_4.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_4.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_4.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_4.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_4.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_4.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_4_win = sip.wrapinstance(self.qtgui_freq_sink_x_4.qwidget(), Qt.QWidget)
        self.tab_layout_5.addWidget(self._qtgui_freq_sink_x_4_win)
        self.qtgui_freq_sink_x_3 = qtgui.freq_sink_c(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_3.set_update_time(0.10)
        self.qtgui_freq_sink_x_3.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_3.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_3.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_3.enable_autoscale(False)
        self.qtgui_freq_sink_x_3.enable_grid(False)
        self.qtgui_freq_sink_x_3.set_fft_average(1.0)
        self.qtgui_freq_sink_x_3.enable_axis_labels(True)
        self.qtgui_freq_sink_x_3.enable_control_panel(False)
        self.qtgui_freq_sink_x_3.set_fft_window_normalized(False)



        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_3.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_3.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_3.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_3.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_3.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_3_win = sip.wrapinstance(self.qtgui_freq_sink_x_3.qwidget(), Qt.QWidget)
        self.tab_layout_3.addWidget(self._qtgui_freq_sink_x_3_win)
        self.qtgui_freq_sink_x_2 = qtgui.freq_sink_c(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_2.set_update_time(0.10)
        self.qtgui_freq_sink_x_2.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_2.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_2.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_2.enable_autoscale(False)
        self.qtgui_freq_sink_x_2.enable_grid(False)
        self.qtgui_freq_sink_x_2.set_fft_average(1.0)
        self.qtgui_freq_sink_x_2.enable_axis_labels(True)
        self.qtgui_freq_sink_x_2.enable_control_panel(False)
        self.qtgui_freq_sink_x_2.set_fft_window_normalized(False)



        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_2.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_2.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_2.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_2.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_2.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_2_win = sip.wrapinstance(self.qtgui_freq_sink_x_2.qwidget(), Qt.QWidget)
        self.tab_layout_0.addWidget(self._qtgui_freq_sink_x_2_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_f(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            400000, #bw
            "", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(0.05)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.qwidget(), Qt.QWidget)
        self.tab_layout_4.addWidget(self._qtgui_freq_sink_x_0_win)
        self.qtgui_eye_sink_x_0_0 = qtgui.eye_sink_f(
            1024, #size
            80000, #samp_rate
            1, #number of inputs
            None
        )
        self.qtgui_eye_sink_x_0_0.set_update_time(0.10)
        self.qtgui_eye_sink_x_0_0.set_samp_per_symbol(sps)
        self.qtgui_eye_sink_x_0_0.set_y_axis(-1, 1)

        self.qtgui_eye_sink_x_0_0.set_y_label('Amplitude', "")

        self.qtgui_eye_sink_x_0_0.enable_tags(True)
        self.qtgui_eye_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_eye_sink_x_0_0.enable_autoscale(False)
        self.qtgui_eye_sink_x_0_0.enable_grid(False)
        self.qtgui_eye_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_eye_sink_x_0_0.enable_control_panel(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'blue', 'blue', 'blue', 'blue',
            'blue', 'blue', 'blue', 'blue', 'blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_eye_sink_x_0_0.set_line_label(i, "Eye[Data {0}]".format(i))
            else:
                self.qtgui_eye_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_eye_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_eye_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_eye_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_eye_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_eye_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_eye_sink_x_0_0_win = sip.wrapinstance(self.qtgui_eye_sink_x_0_0.qwidget(), Qt.QWidget)
        self.tab_layout_8.addWidget(self._qtgui_eye_sink_x_0_0_win)
        self.qtgui_eye_sink_x_0 = qtgui.eye_sink_f(
            1024, #size
            80000, #samp_rate
            1, #number of inputs
            None
        )
        self.qtgui_eye_sink_x_0.set_update_time(0.10)
        self.qtgui_eye_sink_x_0.set_samp_per_symbol(sps)
        self.qtgui_eye_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_eye_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_eye_sink_x_0.enable_tags(True)
        self.qtgui_eye_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_eye_sink_x_0.enable_autoscale(False)
        self.qtgui_eye_sink_x_0.enable_grid(False)
        self.qtgui_eye_sink_x_0.enable_axis_labels(True)
        self.qtgui_eye_sink_x_0.enable_control_panel(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'blue', 'blue', 'blue', 'blue',
            'blue', 'blue', 'blue', 'blue', 'blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_eye_sink_x_0.set_line_label(i, "Eye[Data {0}]".format(i))
            else:
                self.qtgui_eye_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_eye_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_eye_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_eye_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_eye_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_eye_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_eye_sink_x_0_win = sip.wrapinstance(self.qtgui_eye_sink_x_0.qwidget(), Qt.QWidget)
        self.tab_layout_8.addWidget(self._qtgui_eye_sink_x_0_win)
        self.qtgui_const_sink_x_0_0 = qtgui.const_sink_c(
            1024, #size
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0.set_y_axis((-2), 2)
        self.qtgui_const_sink_x_0_0.set_x_axis((-2), 2)
        self.qtgui_const_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0_0.enable_grid(False)
        self.qtgui_const_sink_x_0_0.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0.qwidget(), Qt.QWidget)
        self.tab_layout_2.addWidget(self._qtgui_const_sink_x_0_0_win)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
            1024, #size
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis((-2), 2)
        self.qtgui_const_sink_x_0.set_x_axis((-2), 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.qwidget(), Qt.QWidget)
        self.tab_layout_3.addWidget(self._qtgui_const_sink_x_0_win)
        self._num_range = qtgui.Range(0, 10, 1, 3, 200)
        self._num_win = qtgui.RangeWidget(self._num_range, self.set_num, "'num'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._num_win)
        self.low_pass_filter_0_0_0 = filter.fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                400000,
                50000,
                200,
                window.WIN_HAMMING,
                6.76))
        self.low_pass_filter_0_0 = filter.fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                400000,
                50000,
                200,
                window.WIN_HAMMING,
                6.76))
        self.interp_fir_filter_xxx_0 = filter.interp_fir_filter_ccc(8, [1])
        self.interp_fir_filter_xxx_0.declare_sample_delay(0)
        self.fir_filter_xxx_0_0 = filter.fir_filter_fff(8, [1])
        self.fir_filter_xxx_0_0.declare_sample_delay(0)
        self.fir_filter_xxx_0 = filter.fir_filter_fff(8, [1])
        self.fir_filter_xxx_0.declare_sample_delay(0)
        self.digital_constellation_decoder_cb_0 = digital.constellation_decoder_cb(variable_constellation_0)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc([-1-1j, -1+1j, 1-1j, 1+1j], 1)
        self.blocks_unpack_k_bits_bb_1 = blocks.unpack_k_bits_bb(2)
        self.blocks_unpack_k_bits_bb_0 = blocks.unpack_k_bits_bb(8)
        self.blocks_threshold_ff_0_0 = blocks.threshold_ff((-0.05), 0.05, 0)
        self.blocks_threshold_ff_0 = blocks.threshold_ff((-0.05), 0.05, 0)
        self.blocks_skiphead_0 = blocks.skiphead(gr.sizeof_char*1, 3)
        self.blocks_pack_k_bits_bb_1 = blocks.pack_k_bits_bb(8)
        self.blocks_pack_k_bits_bb_0 = blocks.pack_k_bits_bb(2)
        self.blocks_multiply_xx_3_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_3 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_2 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_moving_average_xx_0_0 = blocks.moving_average_ff(1000, (1e-3), 4000, 1)
        self.blocks_moving_average_xx_0 = blocks.moving_average_ff(1000, (1e-3), 4000, 1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, '/home/nimay/Desktop/Lab_5/Original_Text.txt', True, 0, 0)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, '/home/nimay/Desktop/Lab_6/out_2.txt', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_delay_0_0 = blocks.delay(gr.sizeof_float*1, delay)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, delay)
        self.blocks_complex_to_real_2 = blocks.complex_to_real(1)
        self.blocks_complex_to_imag_1 = blocks.complex_to_imag(1)
        self.blocks_add_xx_1 = blocks.add_vff(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.blocks_abs_xx_0_0 = blocks.abs_ff(1)
        self.blocks_abs_xx_0 = blocks.abs_ff(1)
        self.analog_sig_source_x_0_0 = analog.sig_source_f(400000, analog.GR_SIN_WAVE, 100000, 1, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(400000, analog.GR_COS_WAVE, 100000, 1, 0, 0)
        self.analog_noise_source_x_0 = analog.noise_source_f(analog.GR_GAUSSIAN, 0, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_3, 1))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_2, 1))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_3_0, 1))
        self.connect((self.blocks_abs_xx_0, 0), (self.blocks_moving_average_xx_0, 0))
        self.connect((self.blocks_abs_xx_0_0, 0), (self.blocks_moving_average_xx_0_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_xx_3, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_xx_3_0, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blocks_complex_to_imag_1, 0), (self.blocks_multiply_xx_2, 0))
        self.connect((self.blocks_complex_to_real_2, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_delay_0, 0), (self.fir_filter_xxx_0, 0))
        self.connect((self.blocks_delay_0_0, 0), (self.fir_filter_xxx_0_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_unpack_k_bits_bb_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.digital_constellation_decoder_cb_0, 0))
        self.connect((self.blocks_moving_average_xx_0, 0), (self.qtgui_time_sink_x_0_0_1_0_0_1_1, 0))
        self.connect((self.blocks_moving_average_xx_0_0, 0), (self.qtgui_time_sink_x_0_0_1_0_0_1_1_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_add_xx_1, 0))
        self.connect((self.blocks_multiply_xx_2, 0), (self.blocks_add_xx_1, 1))
        self.connect((self.blocks_multiply_xx_3, 0), (self.low_pass_filter_0_0, 0))
        self.connect((self.blocks_multiply_xx_3_0, 0), (self.low_pass_filter_0_0_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_1, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_skiphead_0, 0), (self.blocks_unpack_k_bits_bb_1, 0))
        self.connect((self.blocks_threshold_ff_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_threshold_ff_0, 0), (self.qtgui_time_sink_x_3_2, 0))
        self.connect((self.blocks_threshold_ff_0_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.blocks_threshold_ff_0_0, 0), (self.qtgui_time_sink_x_3_2_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0, 0), (self.blocks_pack_k_bits_bb_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_1, 0), (self.blocks_pack_k_bits_bb_1, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.interp_fir_filter_xxx_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.qtgui_const_sink_x_0_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.qtgui_freq_sink_x_2, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.qtgui_time_sink_x_1, 0))
        self.connect((self.digital_constellation_decoder_cb_0, 0), (self.blocks_skiphead_0, 0))
        self.connect((self.fir_filter_xxx_0, 0), (self.blocks_abs_xx_0, 0))
        self.connect((self.fir_filter_xxx_0, 0), (self.blocks_threshold_ff_0, 0))
        self.connect((self.fir_filter_xxx_0, 0), (self.qtgui_time_sink_x_3_2_1, 0))
        self.connect((self.fir_filter_xxx_0_0, 0), (self.blocks_abs_xx_0_0, 0))
        self.connect((self.fir_filter_xxx_0_0, 0), (self.blocks_threshold_ff_0_0, 0))
        self.connect((self.fir_filter_xxx_0_0, 0), (self.qtgui_time_sink_x_3_2_1_0, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.root_raised_cosine_filter_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.qtgui_freq_sink_x_6, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.low_pass_filter_0_0_0, 0), (self.qtgui_freq_sink_x_4, 0))
        self.connect((self.low_pass_filter_0_0_0, 0), (self.rational_resampler_xxx_1_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_complex_to_imag_1, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_complex_to_real_2, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.root_raised_cosine_filter_0_0, 0))
        self.connect((self.rational_resampler_xxx_1_0, 0), (self.root_raised_cosine_filter_0_0_0, 0))
        self.connect((self.root_raised_cosine_filter_0, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.root_raised_cosine_filter_0, 0), (self.qtgui_freq_sink_x_3, 0))
        self.connect((self.root_raised_cosine_filter_0, 0), (self.qtgui_time_sink_x_2, 0))
        self.connect((self.root_raised_cosine_filter_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.root_raised_cosine_filter_0_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.root_raised_cosine_filter_0_0, 0), (self.qtgui_eye_sink_x_0, 0))
        self.connect((self.root_raised_cosine_filter_0_0_0, 0), (self.blocks_delay_0_0, 0))
        self.connect((self.root_raised_cosine_filter_0_0_0, 0), (self.qtgui_eye_sink_x_0_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "task_3")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_variable_constellation_0(self):
        return self.variable_constellation_0

    def set_variable_constellation_0(self, variable_constellation_0):
        self.variable_constellation_0 = variable_constellation_0
        self.digital_constellation_decoder_cb_0.set_constellation(self.variable_constellation_0)

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.qtgui_eye_sink_x_0.set_samp_per_symbol(self.sps)
        self.qtgui_eye_sink_x_0_0.set_samp_per_symbol(self.sps)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_freq_sink_x_2.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_3.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_4.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_6.set_frequency_range(0, self.samp_rate)
        self.qtgui_time_sink_x_1.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_2.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_3_2.set_samp_rate(self.samp_rate/2)
        self.qtgui_time_sink_x_3_2_0.set_samp_rate(self.samp_rate/2)
        self.qtgui_time_sink_x_3_2_1.set_samp_rate(self.samp_rate/2)
        self.qtgui_time_sink_x_3_2_1_0.set_samp_rate(self.samp_rate/2)

    def get_num(self):
        return self.num

    def set_num(self, num):
        self.num = num

    def get_delay(self):
        return self.delay

    def set_delay(self, delay):
        self.delay = delay
        self.blocks_delay_0.set_dly(int(self.delay))
        self.blocks_delay_0_0.set_dly(int(self.delay))

    def get_alpha(self):
        return self.alpha

    def set_alpha(self, alpha):
        self.alpha = alpha
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(3, 80000, 10000, self.alpha, (11*8)))
        self.root_raised_cosine_filter_0_0.set_taps(firdes.root_raised_cosine(3, 80000, 10000, self.alpha, 88))
        self.root_raised_cosine_filter_0_0_0.set_taps(firdes.root_raised_cosine(3, 80000, 10000, self.alpha, 88))




def main(top_block_cls=task_3, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
