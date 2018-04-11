# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 15:39:13 2018
Version: python 3.6
@author: MrYanc
"""
import unittest
import ScraperBriefing
import ScraperMarketBeats

class TestScraperMethods(unittest.TestCase):

    def setUp(self):
        self.markbeats = ScraperMarketBeats.MarketBeats();
        self.markbeats.setup();
        self.briefing = ScraperBriefing.Briefing();
        self.briefing.setup();
        pass;

    '''
    function: test ScraperMarketBeats process function
    input: 
    output: 
    exception: 
    '''
    def test_markbeats_process(self):
        start_date = "2018-03-22";
        end_date = "2018-03-24";
        filepath = "D:\\";
        filetype = "xlsx";
        self.assertEqual(self.markbeats.execute(start_date, end_date, filepath, filetype), True, 'Error in MarketBeats Process xlsx');
        filetype = "csv";
        self.assertEqual(self.markbeats.execute(start_date, end_date, filepath, filetype), True, 'Error in MarketBeats Process csv');
        pass;

    '''
    function: test ScraperBriefing process function
    input: 
    output: 
    exception: 
    '''
    def test_briefing_process(self):
        start_date = "2018-03-22";
        end_date = "2018-03-24";
        filepath = "D:\\";
        filetype = "xlsx";
        self.assertEqual(self.briefing.execute(start_date, end_date, filepath, filetype), True, 'Error in Briefing Process xlsx');
        filetype = "csv";
        self.assertEqual(self.briefing.execute(start_date, end_date, filepath, filetype), True, 'Error in Briefing Process csv');
        pass;

    def tearDown(self):
        self.markbeats.dispose();
        self.briefing.dispose();
        pass;

if __name__ == '__main__':
    unittest.main();
    pass;