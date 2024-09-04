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
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import sip



class lab4_q1(gr.top_block, Qt.QWidget):

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

        self.settings = Qt.QSettings("GNU Radio", "lab4_q1")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 4300000
        self.diff_gain = diff_gain = 1
        self.amplitude = amplitude = 0.000001

        ##################################################
        # Blocks
        ##################################################

        self.tab = Qt.QTabWidget()
        self.tab_widget_0 = Qt.QWidget()
        self.tab_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_0)
        self.tab_grid_layout_0 = Qt.QGridLayout()
        self.tab_layout_0.addLayout(self.tab_grid_layout_0)
        self.tab.addTab(self.tab_widget_0, 'Vid')
        self.tab_widget_1 = Qt.QWidget()
        self.tab_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_1)
        self.tab_grid_layout_1 = Qt.QGridLayout()
        self.tab_layout_1.addLayout(self.tab_grid_layout_1)
        self.tab.addTab(self.tab_widget_1, 'Vod')
        self.top_layout.addWidget(self.tab)
        self._amplitude_range = qtgui.Range(0.000001, 0.1, 0.000001, 0.000001, 200)
        self._amplitude_win = qtgui.RangeWidget(self._amplitude_range, self.set_amplitude, "'amplitude'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._amplitude_win)
        self.qtgui_sink_x_1 = qtgui.sink_f(
            1024, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "Vid", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_1.set_update_time(1.0/10)
        self._qtgui_sink_x_1_win = sip.wrapinstance(self.qtgui_sink_x_1.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_1.enable_rf_freq(False)

        self.tab_layout_0.addWidget(self._qtgui_sink_x_1_win)
        self.qtgui_sink_x_0 = qtgui.sink_f(
            1024, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "Vod", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_0.enable_rf_freq(False)

        self.tab_layout_1.addWidget(self._qtgui_sink_x_0_win)
        self.blocks_transcendental_0 = blocks.transcendental('exp', "float")
        self.blocks_throttle2_0 = blocks.throttle( gr.sizeof_float*1, samp_rate, True, 0 if "auto" == "auto" else max( int(float(0.1) * samp_rate) if "auto" == "time" else int(0.1), 1) )
        self.blocks_multiply_const_vxx_3 = blocks.multiply_const_ff(diff_gain)
        self.blocks_multiply_const_vxx_2 = blocks.multiply_const_ff(0.9)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_ff(20)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(amplitude)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_float*1, '/home/nimayshah/Downloads/Input.bin', True, 0, 0)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_divide_xx_0 = blocks.divide_ff(1)
        self.blocks_add_const_vxx_0 = blocks.add_const_ff(1)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_divide_xx_0, 1))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_divide_xx_0, 0))
        self.connect((self.blocks_divide_xx_0, 0), (self.blocks_multiply_const_vxx_3, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_throttle2_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.qtgui_sink_x_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_transcendental_0, 0))
        self.connect((self.blocks_multiply_const_vxx_2, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_3, 0), (self.qtgui_sink_x_0, 0))
        self.connect((self.blocks_throttle2_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_transcendental_0, 0), (self.blocks_multiply_const_vxx_2, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "lab4_q1")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle2_0.set_sample_rate(self.samp_rate)
        self.qtgui_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_sink_x_1.set_frequency_range(0, self.samp_rate)

    def get_diff_gain(self):
        return self.diff_gain

    def set_diff_gain(self, diff_gain):
        self.diff_gain = diff_gain
        self.blocks_multiply_const_vxx_3.set_k(self.diff_gain)

    def get_amplitude(self):
        return self.amplitude

    def set_amplitude(self, amplitude):
        self.amplitude = amplitude
        self.blocks_multiply_const_vxx_0.set_k(self.amplitude)




def main(top_block_cls=lab4_q1, options=None):

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
