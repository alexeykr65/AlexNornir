#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Configure S-Terra
#
# alexeykr@gmail.com
# coding=utf-8
# import codecs
import argparse
import alexnornir.alexnornir as mynor


def check_argument_parser():
    description_argument_parser = ""
    epilog_argument_parser = ""
    parser = argparse.ArgumentParser(description=description_argument_parser, epilog=epilog_argument_parser)
    parser.add_argument('-p', '--ping', help='Ping hosts', dest="ping", action="store_true")
    parser.add_argument('-io', '--info_ospf', help='Get information from OSPF', dest="info_ospf", action="store_true")
    parser.add_argument('-o', '--ospf', help='OSPF Configure Standart ', dest="ospf", action="store_true")
    parser.add_argument('-g', '--getconf', help='Get running Configuration', dest="getconf", action="store_true")
    parser.add_argument('-c', '--cmd', help='Run command on Routers', dest="cmd", default='')
    parser.add_argument('-fr', '--froles', help='Filter hosts by roles', dest="froles", default='')
    parser.add_argument('-fh', '--fhosts', help='Filter hosts by name', dest="fhosts", default='')
    parser.add_argument('-fo', '--fospf', help='Filter for output information in ospf', dest="fospf", default='')
    return parser.parse_args()


def main():
    ag = check_argument_parser()
    nr = mynor.AlexNornir(data_file="src_cfg/dmvpn_data.yaml", filter_hosts=ag.fhosts, filter_roles=ag.froles)
    # nr = mynor.AlexNornir(data_file="src_cfg/dmvpn_data.yaml")
    if ag.ping:
        nr.ping()
    elif ag.cmd:
        nr.run_cmds(ag.cmd)
    elif ag.getconf:
        nr.get_config()
    elif ag.ospf:
        if ag.fospf:
            nr.ospf_filter = ag.fospf
        nr.ospf_info()


if __name__ == '__main__':
    main()
