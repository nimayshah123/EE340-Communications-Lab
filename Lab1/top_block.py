#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: top_block
# GNU Radio version: 3.10.9.2

from PyQt5 import Qt
from gnuradio import qtgui
from PyQt5 import QtCore
from gnuradio import audio
from gnuradio import blocks
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



class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "top_block", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("top_block")
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

        self.settings = Qt.QSettings("GNU Radio", "top_block")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000
        self.a5 = a5 = 1
        self.a4 = a4 = 1
        self.a3 = a3 = 1
        self.a2 = a2 = 1
        self.a1 = a1 = 1

        ##################################################
        # Blocks
        ##################################################

        self._a5_range = qtgui.Range(0, 100, 1, 1, 200)
        self._a5_win = qtgui.RangeWidget(self._a5_range, self.set_a5, "band5", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._a5_win)
        self._a4_range = qtgui.Range(0, 100, 1, 1, 200)
        self._a4_win = qtgui.RangeWidget(self._a4_range, self.set_a4, "bannd4", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._a4_win)
        self._a3_range = qtgui.Range(0, 100, 1, 1, 200)
        self._a3_win = qtgui.RangeWidget(self._a3_range, self.set_a3, "band3", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._a3_win)
        self._a2_range = qtgui.Range(0, 100, 1, 1, 200)
        self._a2_win = qtgui.RangeWidget(self._a2_range, self.set_a2, "band2", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._a2_win)
        self._a1_range = qtgui.Range(0, 10, 1, 1, 200)
        self._a1_win = qtgui.RangeWidget(self._a1_range, self.set_a1, "band1", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._a1_win)
        self.blocks_wavfile_source_0 = blocks.wavfile_source('/home/nimayshah/Downloads/Bach.wav', True)
        self.blocks_throttle2_0 = blocks.throttle( gr.sizeof_float*1, samp_rate, True, 0 if "auto" == "auto" else max( int(float(0.1) * samp_rate) if "auto" == "time" else int(0.1), 1) )
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.band_pass_filter_0_0_0_0_0 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                a5,
                samp_rate,
                9000,
                15000,
                100,
                window.WIN_HAMMING,
                6.76))
        self.band_pass_filter_0_0_0_0 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                a4,
                samp_rate,
                6000,
                9000,
                100,
                window.WIN_HAMMING,
                6.76))
        self.band_pass_filter_0_0_0 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                a3,
                samp_rate,
                3000,
                6000,
                100,
                window.WIN_HAMMING,
                6.76))
        self.band_pass_filter_0_0 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                a2,
                samp_rate,
                500,
                3000,
                50,
                window.WIN_HAMMING,
                6.76))
        self.band_pass_filter_0 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                a1,
                samp_rate,
                20,
                500,
                10,
                window.WIN_HAMMING,
                6.76))
        self.audio_sink_0 = audio.sink(samp_rate, '', True)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.band_pass_filter_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.band_pass_filter_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.band_pass_filter_0_0_0, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.band_pass_filter_0_0_0_0, 0), (self.blocks_add_xx_0, 3))
        self.connect((self.band_pass_filter_0_0_0_0_0, 0), (self.blocks_add_xx_0, 4))
        self.connect((self.blocks_add_xx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_throttle2_0, 0), (self.band_pass_filter_0, 0))
        self.connect((self.blocks_throttle2_0, 0), (self.band_pass_filter_0_0, 0))
        self.connect((self.blocks_throttle2_0, 0), (self.band_pass_filter_0_0_0, 0))
        self.connect((self.blocks_throttle2_0, 0), (self.band_pass_filter_0_0_0_0, 0))
        self.connect((self.blocks_throttle2_0, 0), (self.band_pass_filter_0_0_0_0_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.blocks_throttle2_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.band_pass_filter_0.set_taps(firdes.band_pass(self.a1, self.samp_rate, 20, 500, 10, window.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0.set_taps(firdes.band_pass(self.a2, self.samp_rate, 500, 3000, 50, window.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0.set_taps(firdes.band_pass(self.a3, self.samp_rate, 3000, 6000, 100, window.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0.set_taps(firdes.band_pass(self.a4, self.samp_rate, 6000, 9000, 100, window.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0.set_taps(firdes.band_pass(self.a5, self.samp_rate, 9000, 15000, 100, window.WIN_HAMMING, 6.76))
        self.blocks_throttle2_0.set_sample_rate(self.samp_rate)

    def get_a5(self):
        return self.a5

    def set_a5(self, a5):
        self.a5 = a5
        self.band_pass_filter_0_0_0_0_0.set_taps(firdes.band_pass(self.a5, self.samp_rate, 9000, 15000, 100, window.WIN_HAMMING, 6.76))

    def get_a4(self):
        return self.a4

    def set_a4(self, a4):
        self.a4 = a4
        self.band_pass_filter_0_0_0_0.set_taps(firdes.band_pass(self.a4, self.samp_rate, 6000, 9000, 100, window.WIN_HAMMING, 6.76))

    def get_a3(self):
        return self.a3

    def set_a3(self, a3):
        self.a3 = a3
        self.band_pass_filter_0_0_0.set_taps(firdes.band_pass(self.a3, self.samp_rate, 3000, 6000, 100, window.WIN_HAMMING, 6.76))

    def get_a2(self):
        return self.a2

    def set_a2(self, a2):
        self.a2 = a2
        self.band_pass_filter_0_0.set_taps(firdes.band_pass(self.a2, self.samp_rate, 500, 3000, 50, window.WIN_HAMMING, 6.76))

    def get_a1(self):
        return self.a1

    def set_a1(self, a1):
        self.a1 = a1
        self.band_pass_filter_0.set_taps(firdes.band_pass(self.a1, self.samp_rate, 20, 500, 10, window.WIN_HAMMING, 6.76))




def main(top_block_cls=top_block, options=None):

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
