from __future__ import unicode_literals
import argparse

from pyramid.paster import bootstrap
import transaction

from sfs_ga.interfaces import IMeetingDelegations


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("config_uri", help = "Paster ini file to load settings from")
    parser.add_argument("meeting_from", help = "From-meeting")
    parser.add_argument("meeting_to", help = "To-meeting")
    args = parser.parse_args()
    env = bootstrap(args.config_uri)
    root = env['root']
    meeting_from = root[args.meeting_from]
    meeting_to = root[args.meeting_to]
    print "Creating a copy of delegations"
    print "------------------------------"
    print "From: %s" % args.meeting_from
    print "To:   %s" % args.meeting_to
    print "------------------------------"
    
    new_delegations = IMeetingDelegations(meeting_to)
    for from_delegation in IMeetingDelegations(meeting_from).values():
        new_name = new_delegations.new()
        delegation = new_delegations[new_name]
        print "found %s" % from_delegation.title
        delegation.title = from_delegation.title
    transaction.commit()
    env['closer']()

if __name__ == '__main__':
    main()
