#!/usr/bin/python

import getopt
import mimetypes
import os.path
import sys
import gdata.sample_util
import gdata.sites.client
import gdata.sites.data


SOURCE_APP_NAME = 'googleInc-GoogleSitesAPIPythonLibSample-v1.1'
site_name='testpythonscilab'
client = gdata.sites.client.SitesClient(source=SOURCE_APP_NAME, site=site_name)
try:
	gdata.sample_util.authorize_client(client, service=client.auth_service, source=SOURCE_APP_NAME, scopes=['http://sites.google.com/testpythonscilab/','https://sites.google.com/testpythonscilab/'])
except gdata.client.BadAuthentication:
	exit('Invalid user credentials given.')
except gdata.client.Error:
	exit('Login Error')
	
	
path = '/page1'
print 'Fetching page by its path: ' + path
uri = '%s?path=%s' % (client.MakeContentFeedUri(), path)
:



	
	
	

uri = '%s?kind=%s' % (client.MakeContentFeedUri(),'filecabinet')
feed = client.GetContentFeed(uri=uri)
attachment = client.UploadAttachment('aide_scilab.pdf', feed.entry[3], content_type='application/pdf',
                                     title='Aide mémoire Scilab', description='HR Packet')
print 'Uploaded. View it at: %s' % attachment.GetAlternateLink().href

ms = gdata.data.MediaSource(file_path='/path/to/replacementContent.doc', content_type='application/msword')
existing_attachment.title.text = 'Updated Document Title'
existing_attachment.summary.text = 'version 2.0'

updated_attachment = client.Update(existing_attachment, media_source=ms)
print "Attachment '%s' changed to '%s'" % (existing_attachment.title.text, updated_attachment.title.text)







