#!/usr/bin/python

__author__ = 'e.bidelman (Eric Bidelman)'

import getopt
import mimetypes
import os.path
import sys

import gdata.sample_util
import gdata.sites.client
import gdata.sites.data


SOURCE_APP_NAME = 'googleInc-GoogleSitesAPIPythonLibSample-v1.1'

site_name=None 
site_domain=None

client = gdata.sites.client.SitesClient(source=SOURCE_APP_NAME, site=site_name, domain=site_domain)

self.client.http_client.debug = debug

    try:
      gdata.sample_util.authorize_client(
          self.client, service=self.client.auth_service, source=SOURCE_APP_NAME,
          scopes=['http://sites.google.com/feeds/',
                  'https://sites.google.com/feeds/'])
    except gdata.client.BadAuthentication:
      exit('Invalid user credentials given.')
    except gdata.client.Error:
      exit('Login Error')
      
      
 % choix 6
 
          print "\nFetching filecainets on '%s'...\n" % self.client.site

          uri = '%s?kind=%s' % (self.client.make_content_feed_uri(),
                                'filecabinet')
          feed = self.client.GetContentFeed(uri=uri)

          selection = self.GetChoiceSelection(
              feed, 'Select a filecabinet to upload to: ')

          filepath = raw_input('Enter a filename: ')
          page_title = raw_input('Enter a title for the file: ')
          description = raw_input('Enter a description: ')

          filename = os.path.basename(filepath)
          file_ex = filename[filename.rfind('.'):]
          if not file_ex in mimetypes.types_map:
            content_type = raw_input(
                'Unrecognized file extension. Please enter the mime type: ')
          else:
            content_type = mimetypes.types_map[file_ex]

          entry = None
          if selection is not None:
            entry = feed.entry[selection - 1]

          new_entry = self.client.UploadAttachment(
              filepath, entry, content_type=content_type, title=page_title,
              description=description)
          print 'Uploaded. View it at: %s' % new_entry.GetAlternateLink().href

     
      