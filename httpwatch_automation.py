# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)]
# From type library 'httpwatchprox64.dll'
# On Fri Mar 22 10:52:57 2019
'HttpWatch Professional 11.1 Automation Library'
makepy_version = '0.5.01'
python_version = 0x30702f0

import win32com.client.CLSIDToClass, pythoncom, pywintypes
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch

# The following 3 lines may need tweaking for the particular server
# Candidates are pythoncom.Missing, .Empty and .ArgNotFound
defaultNamedOptArg=pythoncom.Empty
defaultNamedNotOptArg=pythoncom.Empty
defaultUnnamedArg=pythoncom.Empty

CLSID = IID('{494EFA4F-9C46-40A0-A50D-C1D5C8937042}')
MajorVersion = 1
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

from win32com.client import DispatchBaseClass
class CacheInfo(DispatchBaseClass):
	'Provides information about the item in the browser cache'
	CLSID = IID('{30108071-50D2-40B6-9107-D8300B1FA764}')
	coclass_clsid = None

	_prop_map_get_ = {
		"ETag": (1610743815, 2, (8, 0), (), "ETag", None),
		"Expires": (1610743809, 2, (7, 0), (), "Expires", None),
		"HitCount": (1610743816, 2, (3, 0), (), "HitCount", None),
		"IsExpiresSet": (1610743810, 2, (11, 0), (), "IsExpiresSet", None),
		"IsLastAccessSet": (1610743818, 2, (11, 0), (), "IsLastAccessSet", None),
		"IsLastModifiedSet": (1610743814, 2, (11, 0), (), "IsLastModifiedSet", None),
		"IsLastUpdateSet": (1610743817, 2, (11, 0), (), "IsLastUpdateSet", None),
		"LastAccess": (1610743812, 2, (7, 0), (), "LastAccess", None),
		"LastModified": (1610743813, 2, (7, 0), (), "LastModified", None),
		"LastUpdate": (1610743811, 2, (7, 0), (), "LastUpdate", None),
		"URLInCache": (1610743808, 2, (11, 0), (), "URLInCache", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class Chrome(DispatchBaseClass):
	'Used to access Chrome extension'
	CLSID = IID('{09609DDF-174B-478F-A403-DFC01D82F2C3}')
	coclass_clsid = None

	# Result is of type Plugin
	def New(self, chromeChannel=''):
		'Create a new tab within Chrome and access it via HttpWatch'
		return self._ApplyTypes_(1610743808, 1, (9, 32), ((8, 49),), 'New', '{F18298C2-6F2D-417B-8EFA-4A5AC4C64C9A}',chromeChannel
			)

	_prop_map_get_ = {
		"HttpWatchCRXFile": (1610743809, 2, (8, 0), (), "HttpWatchCRXFile", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class Content(DispatchBaseClass):
	'Provides access to the content was read from the cache or downloaded from the server'
	CLSID = IID('{E6086F4F-66DB-40DB-A8BC-11555566A6DA}')
	coclass_clsid = None

	def Export(self, FileName=defaultNamedNotOptArg):
		'Exports the content to the specified file'
		return self._oleobj_.InvokeTypes(1610743815, LCID, 1, (24, 0), ((8, 1),),FileName
			)

	_prop_map_get_ = {
		"CompressedSize": (1610743812, 2, (3, 0), (), "CompressedSize", None),
		"CompressionType": (1610743813, 2, (8, 0), (), "CompressionType", None),
		"Data": (1610743814, 2, (8, 0), (), "Data", None),
		"ImageHeight": (1610743818, 2, (3, 0), (), "ImageHeight", None),
		"ImageWidth": (1610743817, 2, (3, 0), (), "ImageWidth", None),
		"IsCompressed": (1610743811, 2, (11, 0), (), "IsCompressed", None),
		"IsFromCache": (1610743810, 2, (11, 0), (), "IsFromCache", None),
		"IsImage": (1610743816, 2, (11, 0), (), "IsImage", None),
		"MimeType": (1610743808, 2, (8, 0), (), "MimeType", None),
		"Size": (1610743809, 2, (3, 0), (), "Size", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class Cookie(DispatchBaseClass):
	'Represents a cookie that was used in a request or response message'
	CLSID = IID('{0285A8EF-8290-4BCD-9482-7BE19A86136D}')
	coclass_clsid = None

	_prop_map_get_ = {
		"Domain": (1610743810, 2, (8, 0), (), "Domain", None),
		"Expires": (1610743812, 2, (7, 0), (), "Expires", None),
		"IsHttpOnly": (1610743815, 2, (11, 0), (), "IsHttpOnly", None),
		"IsHttpOnlyKnown": (1610743816, 2, (11, 0), (), "IsHttpOnlyKnown", None),
		"IsSecure": (1610743817, 2, (11, 0), (), "IsSecure", None),
		"IsSecureKnown": (1610743818, 2, (11, 0), (), "IsSecureKnown", None),
		"IsSessionCookie": (1610743813, 2, (11, 0), (), "IsSessionCookie", None),
		"Name": (1610743808, 2, (8, 0), (), "Name", None),
		"Path": (1610743811, 2, (8, 0), (), "Path", None),
		"Source": (1610743814, 2, (8, 0), (), "Source", None),
		"Value": (1610743809, 2, (8, 0), (), "Value", None),
	}
	_prop_map_put_ = {
	}
	# Default property for this class is 'Value'
	def __call__(self):
		return self._ApplyTypes_(*(1610743809, 2, (8, 0), (), "Value", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class Cookies(DispatchBaseClass):
	'Contains a list of the cookies use in an HTTP request or response message'
	CLSID = IID('{E8BB54CB-32C4-4E31-BD02-FFF4670201DB}')
	coclass_clsid = None

	# Result is of type Cookie
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, index=defaultNamedNotOptArg):
		'Access individual cookies using a value between 0 and Count - 1'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{0285A8EF-8290-4BCD-9482-7BE19A86136D}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743808, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		'Access individual cookies using a value between 0 and Count - 1'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{0285A8EF-8290-4BCD-9482-7BE19A86136D}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{0285A8EF-8290-4BCD-9482-7BE19A86136D}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743808, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class Entries(DispatchBaseClass):
	'Contains a list of HTTP requests'
	CLSID = IID('{33F42185-77A9-4B0B-833F-2BA039017CBA}')
	coclass_clsid = None

	# Result is of type Entry
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, index=defaultNamedNotOptArg):
		'Access individual entries using a value between 0 and Count - 1'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{F00EDAEF-92F9-4921-BFB2-3BE1FCBE8E66}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743808, 2, (3, 0), (), "Count", None),
		# Method 'Summary' returns object of type 'Summary'
		"Summary": (1610743811, 2, (9, 0), (), "Summary", '{8340029F-30FB-458B-98E2-A9641DC5D0AB}'),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		'Access individual entries using a value between 0 and Count - 1'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{F00EDAEF-92F9-4921-BFB2-3BE1FCBE8E66}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{F00EDAEF-92F9-4921-BFB2-3BE1FCBE8E66}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743808, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class Entry(DispatchBaseClass):
	'Provides access to an HTTP request in the HttpWatch log'
	CLSID = IID('{F00EDAEF-92F9-4921-BFB2-3BE1FCBE8E66}')
	coclass_clsid = None

	_prop_map_get_ = {
		"BytesReceived": (118, 2, (3, 0), (), "BytesReceived", None),
		"BytesSent": (117, 2, (3, 0), (), "BytesSent", None),
		# Method 'CacheAfter' returns object of type 'CacheInfo'
		"CacheAfter": (108, 2, (9, 0), (), "CacheAfter", '{30108071-50D2-40B6-9107-D8300B1FA764}'),
		# Method 'CacheBefore' returns object of type 'CacheInfo'
		"CacheBefore": (107, 2, (9, 0), (), "CacheBefore", '{30108071-50D2-40B6-9107-D8300B1FA764}'),
		"ClientIP": (111, 2, (8, 0), (), "ClientIP", None),
		"ClientPort": (112, 2, (3, 0), (), "ClientPort", None),
		"Comment": (127, 2, (8, 0), (), "Comment", None),
		"ConnectionID": (129, 2, (3, 0), (), "ConnectionID", None),
		# Method 'Content' returns object of type 'Content'
		"Content": (115, 2, (9, 0), (), "Content", '{E6086F4F-66DB-40DB-A8BC-11555566A6DA}'),
		"Error": (121, 2, (8, 0), (), "Error", None),
		"ID": (128, 2, (3, 0), (), "ID", None),
		"IsComplete": (119, 2, (11, 0), (), "IsComplete", None),
		"IsHTTP2": (132, 2, (11, 0), (), "IsHTTP2", None),
		"IsRedirect": (122, 2, (11, 0), (), "IsRedirect", None),
		"IsRestrictedURL": (116, 2, (11, 0), (), "IsRestrictedURL", None),
		"IsSPDY": (130, 2, (11, 0), (), "IsSPDY", None),
		"Method": (101, 2, (8, 0), (), "Method", None),
		# Method 'Page' returns object of type 'Page'
		"Page": (124, 2, (9, 0), (), "Page", '{BE4A78A7-B009-4B09-A2E4-E8EA96159599}'),
		"Protocol": (133, 2, (8, 0), (), "Protocol", None),
		"RedirectURL": (123, 2, (8, 0), (), "RedirectURL", None),
		# Method 'Request' returns object of type 'Request'
		"Request": (113, 2, (9, 0), (), "Request", '{F5234216-06DF-4D7A-A59A-DA4A8F2B0338}'),
		# Method 'Response' returns object of type 'Response'
		"Response": (114, 2, (9, 0), (), "Response", '{BEAF8831-18CF-4B1B-AD18-112C675A2443}'),
		"Result": (106, 2, (8, 0), (), "Result", None),
		"ServerIP": (109, 2, (8, 0), (), "ServerIP", None),
		"ServerPort": (110, 2, (3, 0), (), "ServerPort", None),
		"Started": (102, 2, (8, 0), (), "Started", None),
		"StartedDateTime": (104, 2, (7, 0), (), "StartedDateTime", None),
		"StartedSecs": (103, 2, (5, 0), (), "StartedSecs", None),
		"StatusCode": (120, 2, (3, 0), (), "StatusCode", None),
		"StreamID": (131, 2, (3, 0), (), "StreamID", None),
		"Time": (105, 2, (5, 0), (), "Time", None),
		# Method 'Timings' returns object of type 'Timings'
		"Timings": (125, 2, (9, 0), (), "Timings", '{71F7B683-98D5-4451-B20E-2DEA1E4D22B1}'),
		"URL": (100, 2, (8, 0), (), "URL", None),
		# Method 'Warnings' returns object of type 'Warnings'
		"Warnings": (126, 2, (9, 0), (), "Warnings", '{58A600C1-1413-4972-9A53-2CCD73FE01EC}'),
	}
	_prop_map_put_ = {
		"Comment": ((127, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class Header(DispatchBaseClass):
	'Contains the name and value of a single HTTP header'
	CLSID = IID('{E4B992AF-8CE5-4B3B-8697-EE31916D8DB4}')
	coclass_clsid = None

	_prop_map_get_ = {
		"Name": (1610743808, 2, (8, 0), (), "Name", None),
		"Value": (1610743809, 2, (8, 0), (), "Value", None),
	}
	_prop_map_put_ = {
	}
	# Default property for this class is 'Value'
	def __call__(self):
		return self._ApplyTypes_(*(1610743809, 2, (8, 0), (), "Value", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class Headers(DispatchBaseClass):
	'Contains a list of headers in an HTTP request or response message'
	CLSID = IID('{F9F5CDCD-245F-4666-AD51-B742D1F7296E}')
	coclass_clsid = None

	# Result is of type Header
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, index=defaultNamedNotOptArg):
		'Access individual headers using a value between 0 and Count - 1'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{E4B992AF-8CE5-4B3B-8697-EE31916D8DB4}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743808, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		'Access individual headers using a value between 0 and Count - 1'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{E4B992AF-8CE5-4B3B-8697-EE31916D8DB4}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{E4B992AF-8CE5-4B3B-8697-EE31916D8DB4}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743808, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IController(DispatchBaseClass):
	'The Controller is used to create new instances of HttpWatch and open existing log files'
	CLSID = IID('{F3638BC8-748C-49D7-9E84-B1C3AFCDBFF8}')
	coclass_clsid = IID('{C4CEDB78-2B64-4703-99BE-A037A849D703}')

	# Result is of type Plugin
	def AttachByTitle(self, pageTitle=defaultNamedNotOptArg):
		'Attach HttpWatch to an existing instance of Internet Explorer or Chrome that has a page with the specified title'
		ret = self._oleobj_.InvokeTypes(107, LCID, 1, (9, 0), ((8, 1),),pageTitle
			)
		if ret is not None:
			ret = Dispatch(ret, 'AttachByTitle', '{F18298C2-6F2D-417B-8EFA-4A5AC4C64C9A}')
		return ret

	# Result is of type Log
	def OpenLog(self, FileName=defaultNamedNotOptArg):
		'Opens an HttpWatch log file (.hwl)'
		ret = self._oleobj_.InvokeTypes(102, LCID, 1, (9, 0), ((8, 1),),FileName
			)
		if ret is not None:
			ret = Dispatch(ret, 'OpenLog', '{53BD74EF-9E8B-4575-A8A3-E49A5B8D27FC}')
		return ret

	def Wait(self, Plugin=defaultNamedNotOptArg, timeOutSecs=defaultNamedNotOptArg):
		'Waits for the current page to be downloaded'
		return self._oleobj_.InvokeTypes(103, LCID, 1, (11, 0), ((9, 1), (3, 1)),Plugin
			, timeOutSecs)

	def WaitEx(self, Plugin=defaultNamedNotOptArg, timeOutSecs=defaultNamedNotOptArg, waitForPageLoadEvent=defaultNamedNotOptArg, waitForRenderStartEvent=defaultNamedNotOptArg
			, httpIdleSecs=defaultNamedNotOptArg):
		'Waits for the current page to be downloaded'
		return self._oleobj_.InvokeTypes(106, LCID, 1, (11, 0), ((9, 1), (3, 1), (11, 1), (11, 1), (3, 1)),Plugin
			, timeOutSecs, waitForPageLoadEvent, waitForRenderStartEvent, httpIdleSecs)

	_prop_map_get_ = {
		# Method 'Chrome' returns object of type 'Chrome'
		"Chrome": (108, 2, (9, 0), (), "Chrome", '{09609DDF-174B-478F-A403-DFC01D82F2C3}'),
		# Method 'IE' returns object of type 'IE'
		"IE": (100, 2, (9, 0), (), "IE", '{9F8FEB96-0027-45A8-AC7F-25F1A558F85E}'),
		"IsBasicEdition": (104, 2, (11, 0), (), "IsBasicEdition", None),
		"Version": (105, 2, (8, 0), (), "Version", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IE(DispatchBaseClass):
	'Used to access Internet Explorer plugin'
	CLSID = IID('{9F8FEB96-0027-45A8-AC7F-25F1A558F85E}')
	coclass_clsid = None

	# Result is of type Plugin
	def Attach(self, pBrowser=defaultNamedNotOptArg):
		'Attach HttpWatch to an existing instance of Internet Explorer'
		ret = self._oleobj_.InvokeTypes(1610743808, LCID, 1, (9, 0), ((9, 1),),pBrowser
			)
		if ret is not None:
			ret = Dispatch(ret, 'Attach', '{F18298C2-6F2D-417B-8EFA-4A5AC4C64C9A}')
		return ret

	# Result is of type Plugin
	def New(self):
		'Create a new instance of HttpWatch within IE'
		ret = self._oleobj_.InvokeTypes(1610743809, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'New', '{F18298C2-6F2D-417B-8EFA-4A5AC4C64C9A}')
		return ret

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class Log(DispatchBaseClass):
	'This is a list of HTTP requests that have been recorded in HttpWatch'
	CLSID = IID('{53BD74EF-9E8B-4575-A8A3-E49A5B8D27FC}')
	coclass_clsid = None

	def EnableFilter(self, enable=defaultNamedNotOptArg):
		'Enable or disable the current filter'
		return self._oleobj_.InvokeTypes(100, LCID, 1, (24, 0), ((11, 1),),enable
			)

	def EnableWarningByID(self, warningID=defaultNamedNotOptArg, enable=defaultNamedNotOptArg):
		"Enable or disable a single warning, e.g. 'HW1001'"
		return self._oleobj_.InvokeTypes(125, LCID, 1, (24, 0), ((8, 1), (11, 1)),warningID
			, enable)

	def EnableWarnings(self, enable=defaultNamedNotOptArg):
		'Enable or disable all warnings'
		return self._oleobj_.InvokeTypes(124, LCID, 1, (24, 0), ((11, 1),),enable
			)

	def ExportCSV(self, FileName=defaultNamedNotOptArg):
		'Export the log as CSV'
		return self._oleobj_.InvokeTypes(104, LCID, 1, (24, 0), ((8, 1),),FileName
			)

	def ExportFieldsAsCSV(self, FileName=defaultNamedNotOptArg, fieldList=defaultNamedNotOptArg):
		'Export a set of fields as a CSV file'
		return self._oleobj_.InvokeTypes(123, LCID, 1, (24, 0), ((8, 1), (8, 1)),FileName
			, fieldList)

	def ExportHAR(self, FileName=defaultNamedNotOptArg):
		'Export the log as an HTTP Archive (.HAR)'
		return self._oleobj_.InvokeTypes(119, LCID, 1, (24, 0), ((8, 1),),FileName
			)

	def ExportHAREx(self, FileName=defaultNamedNotOptArg, majorVersion=defaultNamedNotOptArg, minorVersion=defaultNamedNotOptArg, maxTextBodySize=defaultNamedNotOptArg
			, maxBinaryBodySize=defaultNamedNotOptArg):
		'Export the log as an HTTP Archive (.HAR)'
		return self._oleobj_.InvokeTypes(127, LCID, 1, (24, 0), ((8, 1), (3, 1), (3, 1), (3, 1), (3, 1)),FileName
			, majorVersion, minorVersion, maxTextBodySize, maxBinaryBodySize)

	def ExportXML(self, FileName=defaultNamedNotOptArg):
		'Export the log as XML'
		return self._oleobj_.InvokeTypes(103, LCID, 1, (24, 0), ((8, 1),),FileName
			)

	def Save(self, FileName=defaultNamedNotOptArg):
		'Saves the current log to a .hwl file'
		return self._oleobj_.InvokeTypes(102, LCID, 1, (24, 0), ((8, 1),),FileName
			)

	_prop_map_get_ = {
		"BrowserName": (116, 2, (8, 0), (), "BrowserName", None),
		"BrowserVersion": (117, 2, (8, 0), (), "BrowserVersion", None),
		"Comment": (114, 2, (8, 0), (), "Comment", None),
		# Method 'Entries' returns object of type 'Entries'
		"Entries": (108, 2, (9, 0), (), "Entries", '{33F42185-77A9-4B0B-833F-2BA039017CBA}'),
		# Method 'FilteredEntries' returns object of type 'Entries'
		"FilteredEntries": (109, 2, (9, 0), (), "FilteredEntries", '{33F42185-77A9-4B0B-833F-2BA039017CBA}'),
		# Method 'FilteredPages' returns object of type 'Pages'
		"FilteredPages": (107, 2, (9, 0), (), "FilteredPages", '{26B8534B-59E5-4537-AD52-8AB021EDFE34}'),
		"HARVersion": (121, 2, (8, 0), (), "HARVersion", None),
		"HWLVersion": (122, 2, (8, 0), (), "HWLVersion", None),
		"HasNetworkTimings": (110, 2, (11, 0), (), "HasNetworkTimings", None),
		"HasPageGrouping": (111, 2, (11, 0), (), "HasPageGrouping", None),
		"HasTimeZone": (112, 2, (11, 0), (), "HasTimeZone", None),
		"IsFilterEnabled": (101, 2, (11, 0), (), "IsFilterEnabled", None),
		# Method 'Pages' returns object of type 'Pages'
		"Pages": (106, 2, (9, 0), (), "Pages", '{26B8534B-59E5-4537-AD52-8AB021EDFE34}'),
		"RecordedByAppName": (126, 2, (8, 0), (), "RecordedByAppName", None),
		"RecordedByVersion": (118, 2, (8, 0), (), "RecordedByVersion", None),
		"RecordedInBasicEdition": (105, 2, (11, 0), (), "RecordedInBasicEdition", None),
		"TimeZoneOffsetMinutes": (113, 2, (3, 0), (), "TimeZoneOffsetMinutes", None),
		"WasImportedFromHAR": (120, 2, (11, 0), (), "WasImportedFromHAR", None),
	}
	_prop_map_put_ = {
		"Comment": ((114, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class POSTParameter(DispatchBaseClass):
	'Holds the name and value of a POST parameter'
	CLSID = IID('{A065DFB9-32D5-419D-BADB-0BEF567C7C2A}')
	coclass_clsid = None

	def Export(self, FileName=defaultNamedNotOptArg):
		'Exports the contents of the POST parameter to a file'
		return self._oleobj_.InvokeTypes(1610743815, LCID, 1, (24, 0), ((8, 1),),FileName
			)

	_prop_map_get_ = {
		"FileName": (1610743814, 2, (8, 0), (), "FileName", None),
		"IsFile": (1610743813, 2, (11, 0), (), "IsFile", None),
		"IsSizeKnown": (1610743811, 2, (11, 0), (), "IsSizeKnown", None),
		"Name": (1610743808, 2, (8, 0), (), "Name", None),
		"Size": (1610743810, 2, (3, 0), (), "Size", None),
		"Type": (1610743812, 2, (8, 0), (), "Type", None),
		"Value": (1610743809, 2, (8, 0), (), "Value", None),
	}
	_prop_map_put_ = {
	}
	# Default property for this class is 'Value'
	def __call__(self):
		return self._ApplyTypes_(*(1610743809, 2, (8, 0), (), "Value", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class POSTParameters(DispatchBaseClass):
	'Contains a list of POST values sent in an HTTP request message'
	CLSID = IID('{6C1B38A6-9F2C-4DC5-BEFA-629964C5B7F0}')
	coclass_clsid = None

	# Result is of type POSTParameter
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, index=defaultNamedNotOptArg):
		'Access individual POST parameters using a value between 0 and Count - 1'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{A065DFB9-32D5-419D-BADB-0BEF567C7C2A}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743808, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		'Access individual POST parameters using a value between 0 and Count - 1'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{A065DFB9-32D5-419D-BADB-0BEF567C7C2A}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{A065DFB9-32D5-419D-BADB-0BEF567C7C2A}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743808, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class Page(DispatchBaseClass):
	'Provides access to a page in the HttpWatch log'
	CLSID = IID('{BE4A78A7-B009-4B09-A2E4-E8EA96159599}')
	coclass_clsid = None

	_prop_map_get_ = {
		"Comment": (1610743817, 2, (8, 0), (), "Comment", None),
		"Dynamic": (1610743812, 2, (11, 0), (), "Dynamic", None),
		# Method 'Entries' returns object of type 'Entries'
		"Entries": (1610743813, 2, (9, 0), (), "Entries", '{33F42185-77A9-4B0B-833F-2BA039017CBA}'),
		# Method 'Events' returns object of type 'PageEvents'
		"Events": (1610743815, 2, (9, 0), (), "Events", '{5422D39D-A1DD-40EF-A4C2-C36C101D693B}'),
		"IsRestrictedURL": (1610743816, 2, (11, 0), (), "IsRestrictedURL", None),
		"Started": (1610743809, 2, (8, 0), (), "Started", None),
		"StartedDateTime": (1610743811, 2, (7, 0), (), "StartedDateTime", None),
		"StartedSecs": (1610743810, 2, (5, 0), (), "StartedSecs", None),
		"Title": (1610743808, 2, (8, 0), (), "Title", None),
		"Unknown": (1610743814, 2, (11, 0), (), "Unknown", None),
	}
	_prop_map_put_ = {
		"Comment": ((1610743817, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class PageEvent(DispatchBaseClass):
	'Contains a page level timing'
	CLSID = IID('{57602A1E-6929-476F-9CB8-1461432337F3}')
	coclass_clsid = None

	_prop_map_get_ = {
		"Valid": (1610743808, 2, (11, 0), (), "Valid", None),
		"Value": (1610743809, 2, (5, 0), (), "Value", None),
	}
	_prop_map_put_ = {
	}
	# Default property for this class is 'Value'
	def __call__(self):
		return self._ApplyTypes_(*(1610743809, 2, (5, 0), (), "Value", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class PageEvents(DispatchBaseClass):
	'Contains page level event timings'
	CLSID = IID('{5422D39D-A1DD-40EF-A4C2-C36C101D693B}')
	coclass_clsid = None

	_prop_map_get_ = {
		# Method 'DOMLoad' returns object of type 'PageEvent'
		"DOMLoad": (1610743808, 2, (9, 0), (), "DOMLoad", '{57602A1E-6929-476F-9CB8-1461432337F3}'),
		# Method 'HTTPLoad' returns object of type 'PageEvent'
		"HTTPLoad": (1610743810, 2, (9, 0), (), "HTTPLoad", '{57602A1E-6929-476F-9CB8-1461432337F3}'),
		# Method 'PageLoad' returns object of type 'PageEvent'
		"PageLoad": (1610743809, 2, (9, 0), (), "PageLoad", '{57602A1E-6929-476F-9CB8-1461432337F3}'),
		# Method 'RenderStart' returns object of type 'PageEvent'
		"RenderStart": (1610743811, 2, (9, 0), (), "RenderStart", '{57602A1E-6929-476F-9CB8-1461432337F3}'),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class Pages(DispatchBaseClass):
	'Contains a list of pages'
	CLSID = IID('{26B8534B-59E5-4537-AD52-8AB021EDFE34}')
	coclass_clsid = None

	# Result is of type Page
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, index=defaultNamedNotOptArg):
		'Access individual entries using a value between 0 and Count - 1'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{BE4A78A7-B009-4B09-A2E4-E8EA96159599}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743808, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		'Access individual entries using a value between 0 and Count - 1'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{BE4A78A7-B009-4B09-A2E4-E8EA96159599}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{BE4A78A7-B009-4B09-A2E4-E8EA96159599}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743808, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class Plugin(DispatchBaseClass):
	'Used to control the HttpWatch Plugin'
	CLSID = IID('{F18298C2-6F2D-417B-8EFA-4A5AC4C64C9A}')
	coclass_clsid = None

	def Clear(self):
		'Clears the current log'
		return self._oleobj_.InvokeTypes(1610743813, LCID, 1, (24, 0), (),)

	def ClearAllCookies(self):
		'Clear all saved and session cookies'
		return self._oleobj_.InvokeTypes(1610743819, LCID, 1, (24, 0), (),)

	def ClearCache(self):
		'Empty the browser cache'
		return self._oleobj_.InvokeTypes(1610743818, LCID, 1, (24, 0), (),)

	def ClearSessionCookies(self):
		'Clear all session cookies'
		return self._oleobj_.InvokeTypes(1610743820, LCID, 1, (24, 0), (),)

	def CloseBrowser(self):
		'Closes the browser in which HttpWatch is embedded'
		return self._oleobj_.InvokeTypes(1610743833, LCID, 1, (24, 0), (),)

	def CloseWindow(self):
		'Closes the HttpWatch plug-in window'
		return self._oleobj_.InvokeTypes(1610743814, LCID, 1, (24, 0), (),)

	def GotoURL(self, URL=defaultNamedNotOptArg):
		'Go to the specified URL'
		return self._oleobj_.InvokeTypes(1610743816, LCID, 1, (24, 0), ((8, 1),),URL
			)

	def IsLoadingPageEx(self, waitForPageLoadEvent=defaultNamedNotOptArg, waitForRenderStartEvent=defaultNamedNotOptArg, httpIdleSecs=defaultNamedNotOptArg):
		'Indicates if the browser is loading the current page'
		return self._oleobj_.InvokeTypes(1610743834, LCID, 1, (11, 0), ((11, 1), (11, 1), (3, 1)),waitForPageLoadEvent
			, waitForRenderStartEvent, httpIdleSecs)

	def OpenWindow(self, unDocked=defaultNamedNotOptArg):
		'Opens the HttpWatch plug-in window'
		return self._oleobj_.InvokeTypes(1610743815, LCID, 1, (24, 0), ((11, 1),),unDocked
			)

	def Record(self):
		'Starts recording HTTP data'
		return self._oleobj_.InvokeTypes(1610743810, LCID, 1, (24, 0), (),)

	def Stop(self):
		'Stops recording data'
		return self._oleobj_.InvokeTypes(1610743812, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"AutoPurgeDays": (1610743831, 2, (3, 0), (), "AutoPurgeDays", None),
		"AutoRecord": (1610743821, 2, (11, 0), (), "AutoRecord", None),
		"AutoRecordConfirmation": (1610743823, 2, (11, 0), (), "AutoRecordConfirmation", None),
		"AutoSave": (1610743825, 2, (11, 0), (), "AutoSave", None),
		"AutoSavePath": (1610743829, 2, (8, 0), (), "AutoSavePath", None),
		"AutoSaveTimeout": (1610743827, 2, (3, 0), (), "AutoSaveTimeout", None),
		# Method 'Container' returns object of type 'IWebBrowser2'
		"Container": (1610743808, 2, (9, 0), (), "Container", '{D30C1661-CDAF-11D0-8A3E-00C04FC9E26E}'),
		"IsLoadingPage": (1610743817, 2, (11, 0), (), "IsLoadingPage", None),
		"IsRecording": (1610743811, 2, (11, 0), (), "IsRecording", None),
		# Method 'Log' returns object of type 'Log'
		"Log": (1610743809, 2, (9, 0), (), "Log", '{53BD74EF-9E8B-4575-A8A3-E49A5B8D27FC}'),
		"NextPageComment": (1610743835, 2, (8, 0), (), "NextPageComment", None),
	}
	_prop_map_put_ = {
		"AutoPurgeDays": ((1610743831, LCID, 4, 0),()),
		"AutoRecord": ((1610743821, LCID, 4, 0),()),
		"AutoRecordConfirmation": ((1610743823, LCID, 4, 0),()),
		"AutoSave": ((1610743825, LCID, 4, 0),()),
		"AutoSavePath": ((1610743829, LCID, 4, 0),()),
		"AutoSaveTimeout": ((1610743827, LCID, 4, 0),()),
		"NextPageComment": ((1610743835, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class QueryStringValue(DispatchBaseClass):
	'Holds the name and value of a parameter encoded in the querystring section of a URL'
	CLSID = IID('{CE39DFFD-65FF-4B1A-B38D-541D3ECBDBEC}')
	coclass_clsid = None

	_prop_map_get_ = {
		"Name": (1610743808, 2, (8, 0), (), "Name", None),
		"Value": (1610743809, 2, (8, 0), (), "Value", None),
	}
	_prop_map_put_ = {
	}
	# Default property for this class is 'Value'
	def __call__(self):
		return self._ApplyTypes_(*(1610743809, 2, (8, 0), (), "Value", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class QueryStringValues(DispatchBaseClass):
	'Contains a list of the parameters encoded in the querystring section of the URL'
	CLSID = IID('{63A3AEC9-5645-4E59-91DE-6F1E6FFE6B01}')
	coclass_clsid = None

	# Result is of type QueryStringValue
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, index=defaultNamedNotOptArg):
		'Access individual query string parameters using a value between 0 and Count - 1'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{CE39DFFD-65FF-4B1A-B38D-541D3ECBDBEC}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743808, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		'Access individual query string parameters using a value between 0 and Count - 1'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{CE39DFFD-65FF-4B1A-B38D-541D3ECBDBEC}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{CE39DFFD-65FF-4B1A-B38D-541D3ECBDBEC}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743808, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class Request(DispatchBaseClass):
	'Represents the HTTP request message and its contents'
	CLSID = IID('{F5234216-06DF-4D7A-A59A-DA4A8F2B0338}')
	coclass_clsid = None

	_prop_map_get_ = {
		# Method 'Cookies' returns object of type 'Cookies'
		"Cookies": (101, 2, (9, 0), (), "Cookies", '{E8BB54CB-32C4-4E31-BD02-FFF4670201DB}'),
		# Method 'Headers' returns object of type 'Headers'
		"Headers": (102, 2, (9, 0), (), "Headers", '{F9F5CDCD-245F-4666-AD51-B742D1F7296E}'),
		"POSTMimeType": (104, 2, (8, 0), (), "POSTMimeType", None),
		# Method 'POSTParameters' returns object of type 'POSTParameters'
		"POSTParameters": (103, 2, (9, 0), (), "POSTParameters", '{6C1B38A6-9F2C-4DC5-BEFA-629964C5B7F0}'),
		# Method 'QueryStringValues' returns object of type 'QueryStringValues'
		"QueryStringValues": (105, 2, (9, 0), (), "QueryStringValues", '{63A3AEC9-5645-4E59-91DE-6F1E6FFE6B01}'),
		"RequestLine": (100, 2, (8, 0), (), "RequestLine", None),
		"Stream": (106, 2, (8209, 0), (), "Stream", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class Response(DispatchBaseClass):
	'Represents the HTTP response message and its contents'
	CLSID = IID('{BEAF8831-18CF-4B1B-AD18-112C675A2443}')
	coclass_clsid = None

	_prop_map_get_ = {
		"Chunks": (104, 2, (3, 0), (), "Chunks", None),
		# Method 'Cookies' returns object of type 'Cookies'
		"Cookies": (101, 2, (9, 0), (), "Cookies", '{E8BB54CB-32C4-4E31-BD02-FFF4670201DB}'),
		# Method 'Headers' returns object of type 'Headers'
		"Headers": (102, 2, (9, 0), (), "Headers", '{F9F5CDCD-245F-4666-AD51-B742D1F7296E}'),
		"StatusLine": (100, 2, (8, 0), (), "StatusLine", None),
		"Stream": (103, 2, (8209, 0), (), "Stream", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ResultSummaries(DispatchBaseClass):
	'Contains a list of result code or error summaries'
	CLSID = IID('{73A9B44B-0FB6-44F9-BB8A-370EBFC7BF98}')
	coclass_clsid = None

	# Result is of type ResultSummary
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, index=defaultNamedNotOptArg):
		'Access individual entries using a value between 0 and Count - 1'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{237800E5-58C3-4A42-BA42-E84FAEA906AE}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743808, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		'Access individual entries using a value between 0 and Count - 1'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{237800E5-58C3-4A42-BA42-E84FAEA906AE}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{237800E5-58C3-4A42-BA42-E84FAEA906AE}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743808, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ResultSummary(DispatchBaseClass):
	'A list of requests with the same error or status code'
	CLSID = IID('{237800E5-58C3-4A42-BA42-E84FAEA906AE}')
	coclass_clsid = None

	_prop_map_get_ = {
		"Description": (1610743809, 2, (8, 0), (), "Description", None),
		"Occurrences": (1610743810, 2, (3, 0), (), "Occurrences", None),
		"Result": (1610743808, 2, (8, 0), (), "Result", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class Summary(DispatchBaseClass):
	'Provides a summary of a set of requests'
	CLSID = IID('{8340029F-30FB-458B-98E2-A9641DC5D0AB}')
	coclass_clsid = None

	_prop_map_get_ = {
		"AverageHTTPSOverhead": (1610743816, 2, (3, 0), (), "AverageHTTPSOverhead", None),
		"BytesReceived": (1610743811, 2, (3, 0), (), "BytesReceived", None),
		"BytesSent": (1610743810, 2, (3, 0), (), "BytesSent", None),
		"CompressionSavedBytes": (1610743812, 2, (3, 0), (), "CompressionSavedBytes", None),
		"DNSLookUps": (1610743813, 2, (3, 0), (), "DNSLookUps", None),
		# Method 'Errors' returns object of type 'ResultSummaries'
		"Errors": (1610743818, 2, (9, 0), (), "Errors", '{73A9B44B-0FB6-44F9-BB8A-370EBFC7BF98}'),
		"RoundTrips": (1610743809, 2, (3, 0), (), "RoundTrips", None),
		# Method 'StatusCodes' returns object of type 'ResultSummaries'
		"StatusCodes": (1610743817, 2, (9, 0), (), "StatusCodes", '{73A9B44B-0FB6-44F9-BB8A-370EBFC7BF98}'),
		"TCPConnects": (1610743814, 2, (3, 0), (), "TCPConnects", None),
		"Time": (1610743808, 2, (5, 0), (), "Time", None),
		# Method 'TimingSummaries' returns object of type 'TimingSummaries'
		"TimingSummaries": (1610743819, 2, (9, 0), (), "TimingSummaries", '{5EC931D6-6F2D-456E-BE4F-0CF7E0A4A9A3}'),
		"TotalHTTPSOverhead": (1610743815, 2, (3, 0), (), "TotalHTTPSOverhead", None),
		# Method 'WarningSummaries' returns object of type 'WarningSummaries'
		"WarningSummaries": (1610743820, 2, (9, 0), (), "WarningSummaries", '{FB58D46D-06BA-4EDC-AE0A-F0071A1F52FD}'),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class Timing(DispatchBaseClass):
	'Contains a Request Level Timings'
	CLSID = IID('{BBCC50D3-8A27-46C9-A457-4E4B6BF936FD}')
	coclass_clsid = None

	_prop_map_get_ = {
		"Duration": (1610743810, 2, (5, 0), (), "Duration", None),
		"Started": (1610743809, 2, (5, 0), (), "Started", None),
		"Valid": (1610743808, 2, (11, 0), (), "Valid", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class TimingSummaries(DispatchBaseClass):
	'Contains summaries of a timing with a log or page'
	CLSID = IID('{5EC931D6-6F2D-456E-BE4F-0CF7E0A4A9A3}')
	coclass_clsid = None

	_prop_map_get_ = {
		# Method 'Blocked' returns object of type 'TimingSummary'
		"Blocked": (1610743808, 2, (9, 0), (), "Blocked", '{A78CB278-109B-41B2-9971-42A90CB19315}'),
		# Method 'CacheRead' returns object of type 'TimingSummary'
		"CacheRead": (1610743816, 2, (9, 0), (), "CacheRead", '{A78CB278-109B-41B2-9971-42A90CB19315}'),
		# Method 'Connect' returns object of type 'TimingSummary'
		"Connect": (1610743810, 2, (9, 0), (), "Connect", '{A78CB278-109B-41B2-9971-42A90CB19315}'),
		# Method 'DNSLookup' returns object of type 'TimingSummary'
		"DNSLookup": (1610743809, 2, (9, 0), (), "DNSLookup", '{A78CB278-109B-41B2-9971-42A90CB19315}'),
		# Method 'Network' returns object of type 'TimingSummary'
		"Network": (1610743815, 2, (9, 0), (), "Network", '{A78CB278-109B-41B2-9971-42A90CB19315}'),
		# Method 'Receive' returns object of type 'TimingSummary'
		"Receive": (1610743813, 2, (9, 0), (), "Receive", '{A78CB278-109B-41B2-9971-42A90CB19315}'),
		# Method 'SSLHandshake' returns object of type 'TimingSummary'
		"SSLHandshake": (1610743817, 2, (9, 0), (), "SSLHandshake", '{A78CB278-109B-41B2-9971-42A90CB19315}'),
		# Method 'Send' returns object of type 'TimingSummary'
		"Send": (1610743811, 2, (9, 0), (), "Send", '{A78CB278-109B-41B2-9971-42A90CB19315}'),
		# Method 'TTFB' returns object of type 'TimingSummary'
		"TTFB": (1610743814, 2, (9, 0), (), "TTFB", '{A78CB278-109B-41B2-9971-42A90CB19315}'),
		# Method 'Wait' returns object of type 'TimingSummary'
		"Wait": (1610743812, 2, (9, 0), (), "Wait", '{A78CB278-109B-41B2-9971-42A90CB19315}'),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class TimingSummary(DispatchBaseClass):
	'A summary of a timing with a log or page'
	CLSID = IID('{A78CB278-109B-41B2-9971-42A90CB19315}')
	coclass_clsid = None

	_prop_map_get_ = {
		"Average": (1610743811, 2, (5, 0), (), "Average", None),
		"Maximum": (1610743809, 2, (5, 0), (), "Maximum", None),
		"Minimum": (1610743808, 2, (5, 0), (), "Minimum", None),
		"Occurrences": (1610743812, 2, (3, 0), (), "Occurrences", None),
		"Total": (1610743810, 2, (5, 0), (), "Total", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class Timings(DispatchBaseClass):
	'Contains Request Level Timings'
	CLSID = IID('{71F7B683-98D5-4451-B20E-2DEA1E4D22B1}')
	coclass_clsid = None

	_prop_map_get_ = {
		# Method 'Blocked' returns object of type 'Timing'
		"Blocked": (1610743808, 2, (9, 0), (), "Blocked", '{BBCC50D3-8A27-46C9-A457-4E4B6BF936FD}'),
		# Method 'CacheRead' returns object of type 'Timing'
		"CacheRead": (1610743816, 2, (9, 0), (), "CacheRead", '{BBCC50D3-8A27-46C9-A457-4E4B6BF936FD}'),
		# Method 'Connect' returns object of type 'Timing'
		"Connect": (1610743810, 2, (9, 0), (), "Connect", '{BBCC50D3-8A27-46C9-A457-4E4B6BF936FD}'),
		# Method 'DNSLookup' returns object of type 'Timing'
		"DNSLookup": (1610743809, 2, (9, 0), (), "DNSLookup", '{BBCC50D3-8A27-46C9-A457-4E4B6BF936FD}'),
		# Method 'Network' returns object of type 'Timing'
		"Network": (1610743815, 2, (9, 0), (), "Network", '{BBCC50D3-8A27-46C9-A457-4E4B6BF936FD}'),
		# Method 'Receive' returns object of type 'Timing'
		"Receive": (1610743813, 2, (9, 0), (), "Receive", '{BBCC50D3-8A27-46C9-A457-4E4B6BF936FD}'),
		# Method 'SSLHandshake' returns object of type 'Timing'
		"SSLHandshake": (1610743817, 2, (9, 0), (), "SSLHandshake", '{BBCC50D3-8A27-46C9-A457-4E4B6BF936FD}'),
		# Method 'Send' returns object of type 'Timing'
		"Send": (1610743811, 2, (9, 0), (), "Send", '{BBCC50D3-8A27-46C9-A457-4E4B6BF936FD}'),
		# Method 'TTFB' returns object of type 'Timing'
		"TTFB": (1610743814, 2, (9, 0), (), "TTFB", '{BBCC50D3-8A27-46C9-A457-4E4B6BF936FD}'),
		# Method 'Wait' returns object of type 'Timing'
		"Wait": (1610743812, 2, (9, 0), (), "Wait", '{BBCC50D3-8A27-46C9-A457-4E4B6BF936FD}'),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class Warning(DispatchBaseClass):
	'Contains a Warning that was detected for an HTTP request'
	CLSID = IID('{B7A07AA1-F28C-4616-A1E2-6DA53AB39752}')
	coclass_clsid = None

	_prop_map_get_ = {
		"Code": (1610743808, 2, (3, 0), (), "Code", None),
		"Description": (1610743811, 2, (8, 0), (), "Description", None),
		"ID": (1610743809, 2, (8, 0), (), "ID", None),
		"Type": (1610743810, 2, (8, 0), (), "Type", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class WarningSummaries(DispatchBaseClass):
	'Contains a list of warning summaries'
	CLSID = IID('{FB58D46D-06BA-4EDC-AE0A-F0071A1F52FD}')
	coclass_clsid = None

	# Result is of type WarningSummary
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, index=defaultNamedNotOptArg):
		'Access individual entries using a value between 0 and Count - 1'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{77D55250-8974-4C9D-B452-FA611225CC6B}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743808, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		'Access individual entries using a value between 0 and Count - 1'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{77D55250-8974-4C9D-B452-FA611225CC6B}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{77D55250-8974-4C9D-B452-FA611225CC6B}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743808, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class WarningSummary(DispatchBaseClass):
	'Contains a summary of the occurrences of a warning'
	CLSID = IID('{77D55250-8974-4C9D-B452-FA611225CC6B}')
	coclass_clsid = None

	_prop_map_get_ = {
		"Code": (1610743808, 2, (3, 0), (), "Code", None),
		"Description": (1610743811, 2, (8, 0), (), "Description", None),
		"ID": (1610743809, 2, (8, 0), (), "ID", None),
		"Occurrences": (1610743812, 2, (3, 0), (), "Occurrences", None),
		"Type": (1610743810, 2, (8, 0), (), "Type", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class Warnings(DispatchBaseClass):
	'Contains a list of Warnings'
	CLSID = IID('{58A600C1-1413-4972-9A53-2CCD73FE01EC}')
	coclass_clsid = None

	# Result is of type Warning
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, index=defaultNamedNotOptArg):
		'Access individual warnings using a value between 0 and Count - 1'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{B7A07AA1-F28C-4616-A1E2-6DA53AB39752}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743808, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		'Access individual warnings using a value between 0 and Count - 1'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{B7A07AA1-F28C-4616-A1E2-6DA53AB39752}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{B7A07AA1-F28C-4616-A1E2-6DA53AB39752}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743808, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class _IReserved2(DispatchBaseClass):
	'Do not use this interface'
	CLSID = IID('{8BF52022-A0AF-4EA5-A6EB-ABC0D0F2484F}')
	coclass_clsid = None

	def Exec(self, var=defaultNamedNotOptArg):
		'Reserved for use by HttpWatch. Do not use this method'
		return self._oleobj_.InvokeTypes(200, LCID, 1, (24, 0), ((9, 1),),var
			)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _IReserved3(DispatchBaseClass):
	'Do not use this interface'
	CLSID = IID('{CF8B3C81-4F3E-4CBA-ADE6-8CD2C3E778D8}')
	coclass_clsid = None

	def ExecA(self, str=defaultNamedNotOptArg):
		'Reserved for use by HttpWatch. Do not use this method'
		return self._oleobj_.InvokeTypes(201, LCID, 1, (3, 0), ((8, 1),),str
			)

	def ExecA1(self, str=defaultNamedNotOptArg):
		'Reserved for use by HttpWatch. Do not use this method'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(202, LCID, 1, (8, 0), ((8, 1),),str
			)

	def ExecA2(self, str=defaultNamedNotOptArg):
		'Reserved for use by HttpWatch. Do not use this method'
		return self._ApplyTypes_(203, 1, (8209, 0), ((8, 1),), 'ExecA2', None,str
			)

	def ExecB(self, str=defaultNamedNotOptArg, val=defaultNamedNotOptArg):
		'Reserved for use by HttpWatch. Do not use this method'
		return self._oleobj_.InvokeTypes(204, LCID, 1, (24, 0), ((8, 1), (3, 1)),str
			, val)

	def ExecB1(self, str=defaultNamedNotOptArg, val=defaultNamedNotOptArg):
		'Reserved for use by HttpWatch. Do not use this method'
		return self._oleobj_.InvokeTypes(205, LCID, 1, (24, 0), ((8, 1), (8, 1)),str
			, val)

	def ExecB2(self, str=defaultNamedNotOptArg, val=defaultNamedNotOptArg):
		'Reserved for use by HttpWatch. Do not use this method'
		return self._oleobj_.InvokeTypes(206, LCID, 1, (24, 0), ((8, 1), (8209, 1)),str
			, val)

	def ExecB3(self, str=defaultNamedNotOptArg):
		'Reserved for use by HttpWatch. Do not use this method'
		return self._oleobj_.InvokeTypes(207, LCID, 1, (24, 0), ((8, 1),),str
			)

	def ExecC(self, str=defaultNamedNotOptArg, val=defaultNamedNotOptArg):
		'Reserved for use by HttpWatch. Do not use this method'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(208, LCID, 1, (8, 0), ((8, 1), (3, 1)),str
			, val)

	def ExecC1(self, str=defaultNamedNotOptArg, val1=defaultNamedNotOptArg):
		'Reserved for use by HttpWatch. Do not use this method'
		return self._oleobj_.InvokeTypes(209, LCID, 1, (3, 0), ((8, 1), (3, 1)),str
			, val1)

	def ExecC2(self, val=defaultNamedNotOptArg, str=defaultNamedNotOptArg, str1=defaultNamedNotOptArg):
		'Reserved for use by HttpWatch. Do not use this method'
		return self._oleobj_.InvokeTypes(210, LCID, 1, (24, 0), ((3, 1), (8, 1), (8, 1)),val
			, str, str1)

	def ExecC3(self, str=defaultNamedNotOptArg, str1=defaultNamedNotOptArg, str2=defaultNamedNotOptArg, val=defaultNamedNotOptArg):
		'Reserved for use by HttpWatch. Do not use this method'
		return self._oleobj_.InvokeTypes(211, LCID, 1, (24, 0), ((8, 1), (8, 1), (8, 1), (3, 1)),str
			, str1, str2, val)

	def ExecC4(self, val=defaultNamedNotOptArg, str=defaultNamedNotOptArg, pStr2=pythoncom.Missing):
		'Reserved for use by HttpWatch. Do not use this method'
		return self._ApplyTypes_(212, 1, (3, 0), ((3, 1), (8, 1), (16392, 2)), 'ExecC4', None,val
			, str, pStr2)

	def ExecC5(self):
		'Reserved for use by HttpWatch. Do not use this method'
		return self._oleobj_.InvokeTypes(213, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class z_v11_0_IController(DispatchBaseClass):
	'Version 10.0 - 11.0 compatibility interface'
	CLSID = IID('{9EF1CD3C-EFBD-402A-98BF-D9FB9AF510FA}')
	coclass_clsid = None

	# Result is of type Plugin
	def AttachByTitle(self, pageTitle=defaultNamedNotOptArg):
		'Attach HttpWatch to an existing instance of Internet Explorer that has a page with the specified title'
		ret = self._oleobj_.InvokeTypes(107, LCID, 1, (9, 0), ((8, 1),),pageTitle
			)
		if ret is not None:
			ret = Dispatch(ret, 'AttachByTitle', '{F18298C2-6F2D-417B-8EFA-4A5AC4C64C9A}')
		return ret

	# Result is of type Log
	def OpenLog(self, FileName=defaultNamedNotOptArg):
		'Opens an HttpWatch log file (.hwl)'
		ret = self._oleobj_.InvokeTypes(102, LCID, 1, (9, 0), ((8, 1),),FileName
			)
		if ret is not None:
			ret = Dispatch(ret, 'OpenLog', '{53BD74EF-9E8B-4575-A8A3-E49A5B8D27FC}')
		return ret

	def Wait(self, Plugin=defaultNamedNotOptArg, timeOutSecs=defaultNamedNotOptArg):
		'Waits for the current page to be downloaded'
		return self._oleobj_.InvokeTypes(103, LCID, 1, (11, 0), ((9, 1), (3, 1)),Plugin
			, timeOutSecs)

	def WaitEx(self, Plugin=defaultNamedNotOptArg, timeOutSecs=defaultNamedNotOptArg, waitForPageLoadEvent=defaultNamedNotOptArg, waitForRenderStartEvent=defaultNamedNotOptArg
			, httpIdleSecs=defaultNamedNotOptArg):
		'Waits for the current page to be downloaded'
		return self._oleobj_.InvokeTypes(106, LCID, 1, (11, 0), ((9, 1), (3, 1), (11, 1), (11, 1), (3, 1)),Plugin
			, timeOutSecs, waitForPageLoadEvent, waitForRenderStartEvent, httpIdleSecs)

	_prop_map_get_ = {
		"Firefox": (101, 2, (9, 0), (), "Firefox", None),
		# Method 'IE' returns object of type 'IE'
		"IE": (100, 2, (9, 0), (), "IE", '{9F8FEB96-0027-45A8-AC7F-25F1A558F85E}'),
		"IsBasicEdition": (104, 2, (11, 0), (), "IsBasicEdition", None),
		"Version": (105, 2, (8, 0), (), "Version", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class z_v11_1_15_Chrome(DispatchBaseClass):
	'Version compatibility interface'
	CLSID = IID('{599C06FF-EECA-409D-AC55-B6927E6D6886}')
	coclass_clsid = None

	# Result is of type Plugin
	def New(self, chromeChannel=''):
		'Create a new tab within Chrome and access it via HttpWatch'
		return self._ApplyTypes_(1610743808, 1, (9, 32), ((8, 49),), 'New', '{F18298C2-6F2D-417B-8EFA-4A5AC4C64C9A}',chromeChannel
			)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class z_v8_2_Entry(DispatchBaseClass):
	'Version 8.0 - 8.2 compatility interface'
	CLSID = IID('{6BA71A40-892E-4031-9252-BFEB02E340D9}')
	coclass_clsid = None

	_prop_map_get_ = {
		"BytesReceived": (118, 2, (3, 0), (), "BytesReceived", None),
		"BytesSent": (117, 2, (3, 0), (), "BytesSent", None),
		# Method 'CacheAfter' returns object of type 'CacheInfo'
		"CacheAfter": (108, 2, (9, 0), (), "CacheAfter", '{30108071-50D2-40B6-9107-D8300B1FA764}'),
		# Method 'CacheBefore' returns object of type 'CacheInfo'
		"CacheBefore": (107, 2, (9, 0), (), "CacheBefore", '{30108071-50D2-40B6-9107-D8300B1FA764}'),
		"ClientIP": (111, 2, (8, 0), (), "ClientIP", None),
		"ClientPort": (112, 2, (3, 0), (), "ClientPort", None),
		"Comment": (127, 2, (8, 0), (), "Comment", None),
		"ConnectionID": (129, 2, (3, 0), (), "ConnectionID", None),
		# Method 'Content' returns object of type 'Content'
		"Content": (115, 2, (9, 0), (), "Content", '{E6086F4F-66DB-40DB-A8BC-11555566A6DA}'),
		"Error": (121, 2, (8, 0), (), "Error", None),
		"ID": (128, 2, (3, 0), (), "ID", None),
		"IsComplete": (119, 2, (11, 0), (), "IsComplete", None),
		"IsRedirect": (122, 2, (11, 0), (), "IsRedirect", None),
		"IsRestrictedURL": (116, 2, (11, 0), (), "IsRestrictedURL", None),
		"Method": (101, 2, (8, 0), (), "Method", None),
		# Method 'Page' returns object of type 'Page'
		"Page": (124, 2, (9, 0), (), "Page", '{BE4A78A7-B009-4B09-A2E4-E8EA96159599}'),
		"RedirectURL": (123, 2, (8, 0), (), "RedirectURL", None),
		# Method 'Request' returns object of type 'Request'
		"Request": (113, 2, (9, 0), (), "Request", '{F5234216-06DF-4D7A-A59A-DA4A8F2B0338}'),
		# Method 'Response' returns object of type 'Response'
		"Response": (114, 2, (9, 0), (), "Response", '{BEAF8831-18CF-4B1B-AD18-112C675A2443}'),
		"Result": (106, 2, (8, 0), (), "Result", None),
		"ServerIP": (109, 2, (8, 0), (), "ServerIP", None),
		"ServerPort": (110, 2, (3, 0), (), "ServerPort", None),
		"Started": (102, 2, (8, 0), (), "Started", None),
		"StartedDateTime": (104, 2, (7, 0), (), "StartedDateTime", None),
		"StartedSecs": (103, 2, (5, 0), (), "StartedSecs", None),
		"StatusCode": (120, 2, (3, 0), (), "StatusCode", None),
		"Time": (105, 2, (5, 0), (), "Time", None),
		# Method 'Timings' returns object of type 'Timings'
		"Timings": (125, 2, (9, 0), (), "Timings", '{71F7B683-98D5-4451-B20E-2DEA1E4D22B1}'),
		"URL": (100, 2, (8, 0), (), "URL", None),
		# Method 'Warnings' returns object of type 'Warnings'
		"Warnings": (126, 2, (9, 0), (), "Warnings", '{58A600C1-1413-4972-9A53-2CCD73FE01EC}'),
	}
	_prop_map_put_ = {
		"Comment": ((127, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class z_v9_CacheInfo(DispatchBaseClass):
	'Compatibility interface'
	CLSID = IID('{00794C37-D4E1-44D1-9B21-8247A473E061}')
	coclass_clsid = None

	_prop_map_get_ = {
		"ETag": (1610743815, 2, (8, 0), (), "ETag", None),
		"Expires": (1610743809, 2, (7, 0), (), "Expires", None),
		"HitCount": (1610743816, 2, (3, 0), (), "HitCount", None),
		"IsExpiresSet": (1610743810, 2, (11, 0), (), "IsExpiresSet", None),
		"IsLastModifiedSet": (1610743814, 2, (11, 0), (), "IsLastModifiedSet", None),
		"LastAccess": (1610743812, 2, (7, 0), (), "LastAccess", None),
		"LastModified": (1610743813, 2, (7, 0), (), "LastModified", None),
		"LastUpdate": (1610743811, 2, (7, 0), (), "LastUpdate", None),
		"URLInCache": (1610743808, 2, (11, 0), (), "URLInCache", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class z_v9_Entry(DispatchBaseClass):
	'Compatibility Interface'
	CLSID = IID('{C972CF14-E223-48E0-9D25-2BCF1550A74C}')
	coclass_clsid = None

	_prop_map_get_ = {
		"BytesReceived": (118, 2, (3, 0), (), "BytesReceived", None),
		"BytesSent": (117, 2, (3, 0), (), "BytesSent", None),
		# Method 'CacheAfter' returns object of type 'CacheInfo'
		"CacheAfter": (108, 2, (9, 0), (), "CacheAfter", '{30108071-50D2-40B6-9107-D8300B1FA764}'),
		# Method 'CacheBefore' returns object of type 'CacheInfo'
		"CacheBefore": (107, 2, (9, 0), (), "CacheBefore", '{30108071-50D2-40B6-9107-D8300B1FA764}'),
		"ClientIP": (111, 2, (8, 0), (), "ClientIP", None),
		"ClientPort": (112, 2, (3, 0), (), "ClientPort", None),
		"Comment": (127, 2, (8, 0), (), "Comment", None),
		"ConnectionID": (129, 2, (3, 0), (), "ConnectionID", None),
		# Method 'Content' returns object of type 'Content'
		"Content": (115, 2, (9, 0), (), "Content", '{E6086F4F-66DB-40DB-A8BC-11555566A6DA}'),
		"Error": (121, 2, (8, 0), (), "Error", None),
		"ID": (128, 2, (3, 0), (), "ID", None),
		"IsComplete": (119, 2, (11, 0), (), "IsComplete", None),
		"IsRedirect": (122, 2, (11, 0), (), "IsRedirect", None),
		"IsRestrictedURL": (116, 2, (11, 0), (), "IsRestrictedURL", None),
		"IsSPDY": (130, 2, (11, 0), (), "IsSPDY", None),
		"Method": (101, 2, (8, 0), (), "Method", None),
		# Method 'Page' returns object of type 'Page'
		"Page": (124, 2, (9, 0), (), "Page", '{BE4A78A7-B009-4B09-A2E4-E8EA96159599}'),
		"RedirectURL": (123, 2, (8, 0), (), "RedirectURL", None),
		# Method 'Request' returns object of type 'Request'
		"Request": (113, 2, (9, 0), (), "Request", '{F5234216-06DF-4D7A-A59A-DA4A8F2B0338}'),
		# Method 'Response' returns object of type 'Response'
		"Response": (114, 2, (9, 0), (), "Response", '{BEAF8831-18CF-4B1B-AD18-112C675A2443}'),
		"Result": (106, 2, (8, 0), (), "Result", None),
		"SPDYStreamID": (131, 2, (3, 0), (), "SPDYStreamID", None),
		"ServerIP": (109, 2, (8, 0), (), "ServerIP", None),
		"ServerPort": (110, 2, (3, 0), (), "ServerPort", None),
		"Started": (102, 2, (8, 0), (), "Started", None),
		"StartedDateTime": (104, 2, (7, 0), (), "StartedDateTime", None),
		"StartedSecs": (103, 2, (5, 0), (), "StartedSecs", None),
		"StatusCode": (120, 2, (3, 0), (), "StatusCode", None),
		"Time": (105, 2, (5, 0), (), "Time", None),
		# Method 'Timings' returns object of type 'Timings'
		"Timings": (125, 2, (9, 0), (), "Timings", '{71F7B683-98D5-4451-B20E-2DEA1E4D22B1}'),
		"URL": (100, 2, (8, 0), (), "URL", None),
		# Method 'Warnings' returns object of type 'Warnings'
		"Warnings": (126, 2, (9, 0), (), "Warnings", '{58A600C1-1413-4972-9A53-2CCD73FE01EC}'),
	}
	_prop_map_put_ = {
		"Comment": ((127, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class z_v9_TimingSummaries(DispatchBaseClass):
	'Compatibility interface'
	CLSID = IID('{7C121585-EECF-4EB1-9DB0-50D0BB3EE82F}')
	coclass_clsid = None

	_prop_map_get_ = {
		# Method 'Blocked' returns object of type 'TimingSummary'
		"Blocked": (1610743808, 2, (9, 0), (), "Blocked", '{A78CB278-109B-41B2-9971-42A90CB19315}'),
		# Method 'CacheRead' returns object of type 'TimingSummary'
		"CacheRead": (1610743816, 2, (9, 0), (), "CacheRead", '{A78CB278-109B-41B2-9971-42A90CB19315}'),
		# Method 'Connect' returns object of type 'TimingSummary'
		"Connect": (1610743810, 2, (9, 0), (), "Connect", '{A78CB278-109B-41B2-9971-42A90CB19315}'),
		# Method 'DNSLookup' returns object of type 'TimingSummary'
		"DNSLookup": (1610743809, 2, (9, 0), (), "DNSLookup", '{A78CB278-109B-41B2-9971-42A90CB19315}'),
		# Method 'Network' returns object of type 'TimingSummary'
		"Network": (1610743815, 2, (9, 0), (), "Network", '{A78CB278-109B-41B2-9971-42A90CB19315}'),
		# Method 'Receive' returns object of type 'TimingSummary'
		"Receive": (1610743813, 2, (9, 0), (), "Receive", '{A78CB278-109B-41B2-9971-42A90CB19315}'),
		# Method 'Send' returns object of type 'TimingSummary'
		"Send": (1610743811, 2, (9, 0), (), "Send", '{A78CB278-109B-41B2-9971-42A90CB19315}'),
		# Method 'TTFB' returns object of type 'TimingSummary'
		"TTFB": (1610743814, 2, (9, 0), (), "TTFB", '{A78CB278-109B-41B2-9971-42A90CB19315}'),
		# Method 'Wait' returns object of type 'TimingSummary'
		"Wait": (1610743812, 2, (9, 0), (), "Wait", '{A78CB278-109B-41B2-9971-42A90CB19315}'),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class z_v9_Timings(DispatchBaseClass):
	'Compatibiliy interface'
	CLSID = IID('{22E95B79-EAD5-4432-9F2E-05D6F630074F}')
	coclass_clsid = None

	_prop_map_get_ = {
		# Method 'Blocked' returns object of type 'Timing'
		"Blocked": (1610743808, 2, (9, 0), (), "Blocked", '{BBCC50D3-8A27-46C9-A457-4E4B6BF936FD}'),
		# Method 'CacheRead' returns object of type 'Timing'
		"CacheRead": (1610743816, 2, (9, 0), (), "CacheRead", '{BBCC50D3-8A27-46C9-A457-4E4B6BF936FD}'),
		# Method 'Connect' returns object of type 'Timing'
		"Connect": (1610743810, 2, (9, 0), (), "Connect", '{BBCC50D3-8A27-46C9-A457-4E4B6BF936FD}'),
		# Method 'DNSLookup' returns object of type 'Timing'
		"DNSLookup": (1610743809, 2, (9, 0), (), "DNSLookup", '{BBCC50D3-8A27-46C9-A457-4E4B6BF936FD}'),
		# Method 'Network' returns object of type 'Timing'
		"Network": (1610743815, 2, (9, 0), (), "Network", '{BBCC50D3-8A27-46C9-A457-4E4B6BF936FD}'),
		# Method 'Receive' returns object of type 'Timing'
		"Receive": (1610743813, 2, (9, 0), (), "Receive", '{BBCC50D3-8A27-46C9-A457-4E4B6BF936FD}'),
		# Method 'Send' returns object of type 'Timing'
		"Send": (1610743811, 2, (9, 0), (), "Send", '{BBCC50D3-8A27-46C9-A457-4E4B6BF936FD}'),
		# Method 'TTFB' returns object of type 'Timing'
		"TTFB": (1610743814, 2, (9, 0), (), "TTFB", '{BBCC50D3-8A27-46C9-A457-4E4B6BF936FD}'),
		# Method 'Wait' returns object of type 'Timing'
		"Wait": (1610743812, 2, (9, 0), (), "Wait", '{BBCC50D3-8A27-46C9-A457-4E4B6BF936FD}'),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

from win32com.client import CoClassBaseClass
# This CoClass is known by the name 'HttpWatch.Controller'
class Controller(CoClassBaseClass): # A CoClass
	# The Controller is used to create new instances of HttpWatch and open existing log files
	CLSID = IID('{C4CEDB78-2B64-4703-99BE-A037A849D703}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IController,
	]
	default_interface = IController

CacheInfo_vtables_dispatch_ = 1
CacheInfo_vtables_ = [
	(( 'URLInCache' , 'pRet' , ), 1610743808, (1610743808, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Expires' , 'pRet' , ), 1610743809, (1610743809, (), [ (16391, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'IsExpiresSet' , 'pRet' , ), 1610743810, (1610743810, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'LastUpdate' , 'pRet' , ), 1610743811, (1610743811, (), [ (16391, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'LastAccess' , 'pRet' , ), 1610743812, (1610743812, (), [ (16391, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'LastModified' , 'pRet' , ), 1610743813, (1610743813, (), [ (16391, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'IsLastModifiedSet' , 'pRet' , ), 1610743814, (1610743814, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'ETag' , 'pRet' , ), 1610743815, (1610743815, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'HitCount' , 'pRet' , ), 1610743816, (1610743816, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'IsLastUpdateSet' , 'pRet' , ), 1610743817, (1610743817, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'IsLastAccessSet' , 'pRet' , ), 1610743818, (1610743818, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
]

Chrome_vtables_dispatch_ = 1
Chrome_vtables_ = [
	(( 'New' , 'chromeChannel' , 'pRet' , ), 1610743808, (1610743808, (), [ (8, 49, "''", None) , 
			 (16393, 10, None, "IID('{F18298C2-6F2D-417B-8EFA-4A5AC4C64C9A}')") , ], 1 , 1 , 4 , 0 , 56 , (3, 32, None, None) , 0 , )),
	(( 'HttpWatchCRXFile' , 'pRet' , ), 1610743809, (1610743809, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

Content_vtables_dispatch_ = 1
Content_vtables_ = [
	(( 'MimeType' , 'pRet' , ), 1610743808, (1610743808, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Size' , 'pRet' , ), 1610743809, (1610743809, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'IsFromCache' , 'pRet' , ), 1610743810, (1610743810, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'IsCompressed' , 'pRet' , ), 1610743811, (1610743811, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'CompressedSize' , 'pRet' , ), 1610743812, (1610743812, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'CompressionType' , 'pRet' , ), 1610743813, (1610743813, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Data' , 'pRet' , ), 1610743814, (1610743814, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Export' , 'FileName' , ), 1610743815, (1610743815, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'IsImage' , 'pRet' , ), 1610743816, (1610743816, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'ImageWidth' , 'pRet' , ), 1610743817, (1610743817, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'ImageHeight' , 'pRet' , ), 1610743818, (1610743818, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
]

Cookie_vtables_dispatch_ = 1
Cookie_vtables_ = [
	(( 'Name' , 'pRet' , ), 1610743808, (1610743808, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Value' , 'pRet' , ), 1610743809, (1610743809, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Domain' , 'pRet' , ), 1610743810, (1610743810, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Path' , 'pRet' , ), 1610743811, (1610743811, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Expires' , 'pRet' , ), 1610743812, (1610743812, (), [ (16391, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'IsSessionCookie' , 'pRet' , ), 1610743813, (1610743813, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Source' , 'pRet' , ), 1610743814, (1610743814, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'IsHttpOnly' , 'pRet' , ), 1610743815, (1610743815, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'IsHttpOnlyKnown' , 'pRet' , ), 1610743816, (1610743816, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'IsSecure' , 'pRet' , ), 1610743817, (1610743817, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'IsSecureKnown' , 'pRet' , ), 1610743818, (1610743818, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
]

Cookies_vtables_dispatch_ = 1
Cookies_vtables_ = [
	(( 'Count' , 'pRet' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'index' , 'pRet' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{0285A8EF-8290-4BCD-9482-7BE19A86136D}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'pRet' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

Entries_vtables_dispatch_ = 1
Entries_vtables_ = [
	(( 'Count' , 'pRet' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'index' , 'pRet' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{F00EDAEF-92F9-4921-BFB2-3BE1FCBE8E66}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'pRet' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Summary' , 'pRet' , ), 1610743811, (1610743811, (), [ (16393, 10, None, "IID('{8340029F-30FB-458B-98E2-A9641DC5D0AB}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

Entry_vtables_dispatch_ = 1
Entry_vtables_ = [
	(( 'URL' , 'pRet' , ), 100, (100, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Method' , 'pRet' , ), 101, (101, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Started' , 'pRet' , ), 102, (102, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'StartedSecs' , 'pRet' , ), 103, (103, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'StartedDateTime' , 'pRet' , ), 104, (104, (), [ (16391, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Time' , 'pRet' , ), 105, (105, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Result' , 'pRet' , ), 106, (106, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'CacheBefore' , 'pRet' , ), 107, (107, (), [ (16393, 10, None, "IID('{30108071-50D2-40B6-9107-D8300B1FA764}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'CacheAfter' , 'pRet' , ), 108, (108, (), [ (16393, 10, None, "IID('{30108071-50D2-40B6-9107-D8300B1FA764}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'ServerIP' , 'pRet' , ), 109, (109, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'ServerPort' , 'pRet' , ), 110, (110, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'ClientIP' , 'pRet' , ), 111, (111, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'ClientPort' , 'pRet' , ), 112, (112, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Request' , 'pRet' , ), 113, (113, (), [ (16393, 10, None, "IID('{F5234216-06DF-4D7A-A59A-DA4A8F2B0338}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Response' , 'pRet' , ), 114, (114, (), [ (16393, 10, None, "IID('{BEAF8831-18CF-4B1B-AD18-112C675A2443}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Content' , 'pRet' , ), 115, (115, (), [ (16393, 10, None, "IID('{E6086F4F-66DB-40DB-A8BC-11555566A6DA}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'IsRestrictedURL' , 'pRet' , ), 116, (116, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'BytesSent' , 'pRet' , ), 117, (117, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'BytesReceived' , 'pRet' , ), 118, (118, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'IsComplete' , 'pRet' , ), 119, (119, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'StatusCode' , 'pRet' , ), 120, (120, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Error' , 'pRet' , ), 121, (121, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'IsRedirect' , 'pRet' , ), 122, (122, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'RedirectURL' , 'pRet' , ), 123, (123, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Page' , 'pRet' , ), 124, (124, (), [ (16393, 10, None, "IID('{BE4A78A7-B009-4B09-A2E4-E8EA96159599}')") , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Timings' , 'pRet' , ), 125, (125, (), [ (16393, 10, None, "IID('{71F7B683-98D5-4451-B20E-2DEA1E4D22B1}')") , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Warnings' , 'pRet' , ), 126, (126, (), [ (16393, 10, None, "IID('{58A600C1-1413-4972-9A53-2CCD73FE01EC}')") , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'Comment' , 'pOut' , ), 127, (127, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Comment' , 'pOut' , ), 127, (127, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'ID' , 'pRet' , ), 128, (128, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'ConnectionID' , 'pRet' , ), 129, (129, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'IsSPDY' , 'pRet' , ), 130, (130, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'StreamID' , 'pRet' , ), 131, (131, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'IsHTTP2' , 'pRet' , ), 132, (132, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'Protocol' , 'pOut' , ), 133, (133, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
]

Header_vtables_dispatch_ = 1
Header_vtables_ = [
	(( 'Name' , 'pRet' , ), 1610743808, (1610743808, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Value' , 'pRet' , ), 1610743809, (1610743809, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

Headers_vtables_dispatch_ = 1
Headers_vtables_ = [
	(( 'Count' , 'pRet' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'index' , 'pRet' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{E4B992AF-8CE5-4B3B-8697-EE31916D8DB4}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'pRet' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IController_vtables_dispatch_ = 1
IController_vtables_ = [
	(( 'IE' , 'pRet' , ), 100, (100, (), [ (16393, 10, None, "IID('{9F8FEB96-0027-45A8-AC7F-25F1A558F85E}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'OpenLog' , 'FileName' , 'pRet' , ), 102, (102, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{53BD74EF-9E8B-4575-A8A3-E49A5B8D27FC}')") , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Wait' , 'Plugin' , 'timeOutSecs' , 'pRet' , ), 103, (103, (), [ 
			 (9, 1, None, "IID('{F18298C2-6F2D-417B-8EFA-4A5AC4C64C9A}')") , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'IsBasicEdition' , 'pRet' , ), 104, (104, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Version' , 'pRet' , ), 105, (105, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'WaitEx' , 'Plugin' , 'timeOutSecs' , 'waitForPageLoadEvent' , 'waitForRenderStartEvent' , 
			 'httpIdleSecs' , 'pRet' , ), 106, (106, (), [ (9, 1, None, "IID('{F18298C2-6F2D-417B-8EFA-4A5AC4C64C9A}')") , (3, 1, None, None) , 
			 (11, 1, None, None) , (11, 1, None, None) , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'AttachByTitle' , 'pageTitle' , 'pRet' , ), 107, (107, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{F18298C2-6F2D-417B-8EFA-4A5AC4C64C9A}')") , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Chrome' , 'pRet' , ), 108, (108, (), [ (16393, 10, None, "IID('{09609DDF-174B-478F-A403-DFC01D82F2C3}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

IE_vtables_dispatch_ = 1
IE_vtables_ = [
	(( 'Attach' , 'pBrowser' , 'pRet' , ), 1610743808, (1610743808, (), [ (9, 1, None, "IID('{D30C1661-CDAF-11D0-8A3E-00C04FC9E26E}')") , 
			 (16393, 10, None, "IID('{F18298C2-6F2D-417B-8EFA-4A5AC4C64C9A}')") , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'New' , 'pRet' , ), 1610743809, (1610743809, (), [ (16393, 10, None, "IID('{F18298C2-6F2D-417B-8EFA-4A5AC4C64C9A}')") , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

Log_vtables_dispatch_ = 1
Log_vtables_ = [
	(( 'EnableFilter' , 'enable' , ), 100, (100, (), [ (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'IsFilterEnabled' , 'pRet' , ), 101, (101, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Save' , 'FileName' , ), 102, (102, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'ExportXML' , 'FileName' , ), 103, (103, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'ExportCSV' , 'FileName' , ), 104, (104, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'RecordedInBasicEdition' , 'pRet' , ), 105, (105, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Pages' , 'pOut' , ), 106, (106, (), [ (16393, 10, None, "IID('{26B8534B-59E5-4537-AD52-8AB021EDFE34}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'FilteredPages' , 'pOut' , ), 107, (107, (), [ (16393, 10, None, "IID('{26B8534B-59E5-4537-AD52-8AB021EDFE34}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Entries' , 'pOut' , ), 108, (108, (), [ (16393, 10, None, "IID('{33F42185-77A9-4B0B-833F-2BA039017CBA}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'FilteredEntries' , 'pOut' , ), 109, (109, (), [ (16393, 10, None, "IID('{33F42185-77A9-4B0B-833F-2BA039017CBA}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'HasNetworkTimings' , 'pOut' , ), 110, (110, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'HasPageGrouping' , 'pOut' , ), 111, (111, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'HasTimeZone' , 'pOut' , ), 112, (112, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'TimeZoneOffsetMinutes' , 'pOut' , ), 113, (113, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Comment' , 'pOut' , ), 114, (114, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Comment' , 'pOut' , ), 114, (114, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'BrowserName' , 'pOut' , ), 116, (116, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'BrowserVersion' , 'pOut' , ), 117, (117, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'RecordedByVersion' , 'pOut' , ), 118, (118, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'ExportHAR' , 'FileName' , ), 119, (119, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'WasImportedFromHAR' , 'pRet' , ), 120, (120, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'HARVersion' , 'pRet' , ), 121, (121, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'HWLVersion' , 'pRet' , ), 122, (122, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'ExportFieldsAsCSV' , 'FileName' , 'fieldList' , ), 123, (123, (), [ (8, 1, None, None) , 
			 (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'EnableWarnings' , 'enable' , ), 124, (124, (), [ (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'EnableWarningByID' , 'warningID' , 'enable' , ), 125, (125, (), [ (8, 1, None, None) , 
			 (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'RecordedByAppName' , 'pOut' , ), 126, (126, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'ExportHAREx' , 'FileName' , 'majorVersion' , 'minorVersion' , 'maxTextBodySize' , 
			 'maxBinaryBodySize' , ), 127, (127, (), [ (8, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , 
			 (3, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
]

POSTParameter_vtables_dispatch_ = 1
POSTParameter_vtables_ = [
	(( 'Name' , 'pRet' , ), 1610743808, (1610743808, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Value' , 'pRet' , ), 1610743809, (1610743809, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Size' , 'pRet' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'IsSizeKnown' , 'pRet' , ), 1610743811, (1610743811, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'pRet' , ), 1610743812, (1610743812, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'IsFile' , 'pRet' , ), 1610743813, (1610743813, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'FileName' , 'pRet' , ), 1610743814, (1610743814, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Export' , 'FileName' , ), 1610743815, (1610743815, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

POSTParameters_vtables_dispatch_ = 1
POSTParameters_vtables_ = [
	(( 'Count' , 'pRet' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'index' , 'pRet' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{A065DFB9-32D5-419D-BADB-0BEF567C7C2A}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'pRet' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

Page_vtables_dispatch_ = 1
Page_vtables_ = [
	(( 'Title' , 'pRet' , ), 1610743808, (1610743808, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Started' , 'pRet' , ), 1610743809, (1610743809, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'StartedSecs' , 'pRet' , ), 1610743810, (1610743810, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'StartedDateTime' , 'pRet' , ), 1610743811, (1610743811, (), [ (16391, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Dynamic' , 'pRet' , ), 1610743812, (1610743812, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Entries' , 'pRet' , ), 1610743813, (1610743813, (), [ (16393, 10, None, "IID('{33F42185-77A9-4B0B-833F-2BA039017CBA}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Unknown' , 'pRet' , ), 1610743814, (1610743814, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Events' , 'pRet' , ), 1610743815, (1610743815, (), [ (16393, 10, None, "IID('{5422D39D-A1DD-40EF-A4C2-C36C101D693B}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'IsRestrictedURL' , 'pRet' , ), 1610743816, (1610743816, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Comment' , 'pOut' , ), 1610743817, (1610743817, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Comment' , 'pOut' , ), 1610743817, (1610743817, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
]

PageEvent_vtables_dispatch_ = 1
PageEvent_vtables_ = [
	(( 'Valid' , 'pRet' , ), 1610743808, (1610743808, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Value' , 'pRet' , ), 1610743809, (1610743809, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

PageEvents_vtables_dispatch_ = 1
PageEvents_vtables_ = [
	(( 'DOMLoad' , 'pRet' , ), 1610743808, (1610743808, (), [ (16393, 10, None, "IID('{57602A1E-6929-476F-9CB8-1461432337F3}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'PageLoad' , 'pRet' , ), 1610743809, (1610743809, (), [ (16393, 10, None, "IID('{57602A1E-6929-476F-9CB8-1461432337F3}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'HTTPLoad' , 'pRet' , ), 1610743810, (1610743810, (), [ (16393, 10, None, "IID('{57602A1E-6929-476F-9CB8-1461432337F3}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'RenderStart' , 'pRet' , ), 1610743811, (1610743811, (), [ (16393, 10, None, "IID('{57602A1E-6929-476F-9CB8-1461432337F3}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

Pages_vtables_dispatch_ = 1
Pages_vtables_ = [
	(( 'Count' , 'pRet' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'index' , 'pRet' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{BE4A78A7-B009-4B09-A2E4-E8EA96159599}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'pRet' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

Plugin_vtables_dispatch_ = 1
Plugin_vtables_ = [
	(( 'Container' , 'pRet' , ), 1610743808, (1610743808, (), [ (16393, 10, None, "IID('{D30C1661-CDAF-11D0-8A3E-00C04FC9E26E}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Log' , 'pRet' , ), 1610743809, (1610743809, (), [ (16393, 10, None, "IID('{53BD74EF-9E8B-4575-A8A3-E49A5B8D27FC}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Record' , ), 1610743810, (1610743810, (), [ ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'IsRecording' , 'pRet' , ), 1610743811, (1610743811, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Stop' , ), 1610743812, (1610743812, (), [ ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Clear' , ), 1610743813, (1610743813, (), [ ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'CloseWindow' , ), 1610743814, (1610743814, (), [ ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'OpenWindow' , 'unDocked' , ), 1610743815, (1610743815, (), [ (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'GotoURL' , 'URL' , ), 1610743816, (1610743816, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'IsLoadingPage' , 'pRet' , ), 1610743817, (1610743817, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'ClearCache' , ), 1610743818, (1610743818, (), [ ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'ClearAllCookies' , ), 1610743819, (1610743819, (), [ ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'ClearSessionCookies' , ), 1610743820, (1610743820, (), [ ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'AutoRecord' , 'pRet' , ), 1610743821, (1610743821, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'AutoRecord' , 'pRet' , ), 1610743821, (1610743821, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'AutoRecordConfirmation' , 'pRet' , ), 1610743823, (1610743823, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'AutoRecordConfirmation' , 'pRet' , ), 1610743823, (1610743823, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'AutoSave' , 'pRet' , ), 1610743825, (1610743825, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'AutoSave' , 'pRet' , ), 1610743825, (1610743825, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'AutoSaveTimeout' , 'pRet' , ), 1610743827, (1610743827, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'AutoSaveTimeout' , 'pRet' , ), 1610743827, (1610743827, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'AutoSavePath' , 'pRet' , ), 1610743829, (1610743829, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'AutoSavePath' , 'pRet' , ), 1610743829, (1610743829, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'AutoPurgeDays' , 'pRet' , ), 1610743831, (1610743831, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'AutoPurgeDays' , 'pRet' , ), 1610743831, (1610743831, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'CloseBrowser' , ), 1610743833, (1610743833, (), [ ], 1 , 1 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'IsLoadingPageEx' , 'waitForPageLoadEvent' , 'waitForRenderStartEvent' , 'httpIdleSecs' , 'pRet' , 
			 ), 1610743834, (1610743834, (), [ (11, 1, None, None) , (11, 1, None, None) , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'NextPageComment' , 'pOut' , ), 1610743835, (1610743835, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'NextPageComment' , 'pOut' , ), 1610743835, (1610743835, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
]

QueryStringValue_vtables_dispatch_ = 1
QueryStringValue_vtables_ = [
	(( 'Name' , 'pRet' , ), 1610743808, (1610743808, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Value' , 'pRet' , ), 1610743809, (1610743809, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

QueryStringValues_vtables_dispatch_ = 1
QueryStringValues_vtables_ = [
	(( 'Count' , 'pRet' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'index' , 'pRet' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{CE39DFFD-65FF-4B1A-B38D-541D3ECBDBEC}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'pRet' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

Request_vtables_dispatch_ = 1
Request_vtables_ = [
	(( 'RequestLine' , 'pRet' , ), 100, (100, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Cookies' , 'pRet' , ), 101, (101, (), [ (16393, 10, None, "IID('{E8BB54CB-32C4-4E31-BD02-FFF4670201DB}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Headers' , 'pRet' , ), 102, (102, (), [ (16393, 10, None, "IID('{F9F5CDCD-245F-4666-AD51-B742D1F7296E}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'POSTParameters' , 'pRet' , ), 103, (103, (), [ (16393, 10, None, "IID('{6C1B38A6-9F2C-4DC5-BEFA-629964C5B7F0}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'POSTMimeType' , 'pRet' , ), 104, (104, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'QueryStringValues' , 'pRet' , ), 105, (105, (), [ (16393, 10, None, "IID('{63A3AEC9-5645-4E59-91DE-6F1E6FFE6B01}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Stream' , 'pVal' , ), 106, (106, (), [ (24593, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
]

Response_vtables_dispatch_ = 1
Response_vtables_ = [
	(( 'StatusLine' , 'pRet' , ), 100, (100, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Cookies' , 'pRet' , ), 101, (101, (), [ (16393, 10, None, "IID('{E8BB54CB-32C4-4E31-BD02-FFF4670201DB}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Headers' , 'pRet' , ), 102, (102, (), [ (16393, 10, None, "IID('{F9F5CDCD-245F-4666-AD51-B742D1F7296E}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Stream' , 'pVal' , ), 103, (103, (), [ (24593, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Chunks' , 'pRet' , ), 104, (104, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

ResultSummaries_vtables_dispatch_ = 1
ResultSummaries_vtables_ = [
	(( 'Count' , 'pRet' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'index' , 'pRet' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{237800E5-58C3-4A42-BA42-E84FAEA906AE}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'pRet' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

ResultSummary_vtables_dispatch_ = 1
ResultSummary_vtables_ = [
	(( 'Result' , 'pRet' , ), 1610743808, (1610743808, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Description' , 'pRet' , ), 1610743809, (1610743809, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Occurrences' , 'pRet' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

Summary_vtables_dispatch_ = 1
Summary_vtables_ = [
	(( 'Time' , 'pRet' , ), 1610743808, (1610743808, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'RoundTrips' , 'pRet' , ), 1610743809, (1610743809, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'BytesSent' , 'pRet' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'BytesReceived' , 'pRet' , ), 1610743811, (1610743811, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'CompressionSavedBytes' , 'pRet' , ), 1610743812, (1610743812, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'DNSLookUps' , 'pRet' , ), 1610743813, (1610743813, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'TCPConnects' , 'pRet' , ), 1610743814, (1610743814, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'TotalHTTPSOverhead' , 'pRet' , ), 1610743815, (1610743815, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'AverageHTTPSOverhead' , 'pRet' , ), 1610743816, (1610743816, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'StatusCodes' , 'pRet' , ), 1610743817, (1610743817, (), [ (16393, 10, None, "IID('{73A9B44B-0FB6-44F9-BB8A-370EBFC7BF98}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Errors' , 'pRet' , ), 1610743818, (1610743818, (), [ (16393, 10, None, "IID('{73A9B44B-0FB6-44F9-BB8A-370EBFC7BF98}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'TimingSummaries' , 'pRet' , ), 1610743819, (1610743819, (), [ (16393, 10, None, "IID('{5EC931D6-6F2D-456E-BE4F-0CF7E0A4A9A3}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'WarningSummaries' , 'pRet' , ), 1610743820, (1610743820, (), [ (16393, 10, None, "IID('{FB58D46D-06BA-4EDC-AE0A-F0071A1F52FD}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
]

Timing_vtables_dispatch_ = 1
Timing_vtables_ = [
	(( 'Valid' , 'pRet' , ), 1610743808, (1610743808, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Started' , 'pRet' , ), 1610743809, (1610743809, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Duration' , 'pRet' , ), 1610743810, (1610743810, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

TimingSummaries_vtables_dispatch_ = 1
TimingSummaries_vtables_ = [
	(( 'Blocked' , 'pRet' , ), 1610743808, (1610743808, (), [ (16393, 10, None, "IID('{A78CB278-109B-41B2-9971-42A90CB19315}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'DNSLookup' , 'pRet' , ), 1610743809, (1610743809, (), [ (16393, 10, None, "IID('{A78CB278-109B-41B2-9971-42A90CB19315}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Connect' , 'pRet' , ), 1610743810, (1610743810, (), [ (16393, 10, None, "IID('{A78CB278-109B-41B2-9971-42A90CB19315}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Send' , 'pRet' , ), 1610743811, (1610743811, (), [ (16393, 10, None, "IID('{A78CB278-109B-41B2-9971-42A90CB19315}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Wait' , 'pRet' , ), 1610743812, (1610743812, (), [ (16393, 10, None, "IID('{A78CB278-109B-41B2-9971-42A90CB19315}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Receive' , 'pRet' , ), 1610743813, (1610743813, (), [ (16393, 10, None, "IID('{A78CB278-109B-41B2-9971-42A90CB19315}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'TTFB' , 'pRet' , ), 1610743814, (1610743814, (), [ (16393, 10, None, "IID('{A78CB278-109B-41B2-9971-42A90CB19315}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Network' , 'pRet' , ), 1610743815, (1610743815, (), [ (16393, 10, None, "IID('{A78CB278-109B-41B2-9971-42A90CB19315}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'CacheRead' , 'pRet' , ), 1610743816, (1610743816, (), [ (16393, 10, None, "IID('{A78CB278-109B-41B2-9971-42A90CB19315}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'SSLHandshake' , 'pRet' , ), 1610743817, (1610743817, (), [ (16393, 10, None, "IID('{A78CB278-109B-41B2-9971-42A90CB19315}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
]

TimingSummary_vtables_dispatch_ = 1
TimingSummary_vtables_ = [
	(( 'Minimum' , 'pRet' , ), 1610743808, (1610743808, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Maximum' , 'pRet' , ), 1610743809, (1610743809, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Total' , 'pRet' , ), 1610743810, (1610743810, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Average' , 'pRet' , ), 1610743811, (1610743811, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Occurrences' , 'pRet' , ), 1610743812, (1610743812, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

Timings_vtables_dispatch_ = 1
Timings_vtables_ = [
	(( 'Blocked' , 'pRet' , ), 1610743808, (1610743808, (), [ (16393, 10, None, "IID('{BBCC50D3-8A27-46C9-A457-4E4B6BF936FD}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'DNSLookup' , 'pRet' , ), 1610743809, (1610743809, (), [ (16393, 10, None, "IID('{BBCC50D3-8A27-46C9-A457-4E4B6BF936FD}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Connect' , 'pRet' , ), 1610743810, (1610743810, (), [ (16393, 10, None, "IID('{BBCC50D3-8A27-46C9-A457-4E4B6BF936FD}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Send' , 'pRet' , ), 1610743811, (1610743811, (), [ (16393, 10, None, "IID('{BBCC50D3-8A27-46C9-A457-4E4B6BF936FD}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Wait' , 'pRet' , ), 1610743812, (1610743812, (), [ (16393, 10, None, "IID('{BBCC50D3-8A27-46C9-A457-4E4B6BF936FD}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Receive' , 'pRet' , ), 1610743813, (1610743813, (), [ (16393, 10, None, "IID('{BBCC50D3-8A27-46C9-A457-4E4B6BF936FD}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'TTFB' , 'pRet' , ), 1610743814, (1610743814, (), [ (16393, 10, None, "IID('{BBCC50D3-8A27-46C9-A457-4E4B6BF936FD}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Network' , 'pRet' , ), 1610743815, (1610743815, (), [ (16393, 10, None, "IID('{BBCC50D3-8A27-46C9-A457-4E4B6BF936FD}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'CacheRead' , 'pRet' , ), 1610743816, (1610743816, (), [ (16393, 10, None, "IID('{BBCC50D3-8A27-46C9-A457-4E4B6BF936FD}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'SSLHandshake' , 'pRet' , ), 1610743817, (1610743817, (), [ (16393, 10, None, "IID('{BBCC50D3-8A27-46C9-A457-4E4B6BF936FD}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
]

Warning_vtables_dispatch_ = 1
Warning_vtables_ = [
	(( 'Code' , 'pRet' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'ID' , 'pRet' , ), 1610743809, (1610743809, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'pRet' , ), 1610743810, (1610743810, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Description' , 'pRet' , ), 1610743811, (1610743811, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

WarningSummaries_vtables_dispatch_ = 1
WarningSummaries_vtables_ = [
	(( 'Count' , 'pRet' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'index' , 'pRet' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{77D55250-8974-4C9D-B452-FA611225CC6B}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'pRet' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

WarningSummary_vtables_dispatch_ = 1
WarningSummary_vtables_ = [
	(( 'Code' , 'pRet' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'ID' , 'pRet' , ), 1610743809, (1610743809, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'pRet' , ), 1610743810, (1610743810, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Description' , 'pRet' , ), 1610743811, (1610743811, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Occurrences' , 'pRet' , ), 1610743812, (1610743812, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

Warnings_vtables_dispatch_ = 1
Warnings_vtables_ = [
	(( 'Count' , 'pRet' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'index' , 'pRet' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{B7A07AA1-F28C-4616-A1E2-6DA53AB39752}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'pRet' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

_IReserved2_vtables_dispatch_ = 1
_IReserved2_vtables_ = [
	(( 'Exec' , 'var' , ), 200, (200, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
]

_IReserved3_vtables_dispatch_ = 1
_IReserved3_vtables_ = [
	(( 'ExecA' , 'str' , 'pRet' , ), 201, (201, (), [ (8, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'ExecA1' , 'str' , 'pRet' , ), 202, (202, (), [ (8, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'ExecA2' , 'str' , 'pRet' , ), 203, (203, (), [ (8, 1, None, None) , 
			 (24593, 10, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'ExecB' , 'str' , 'val' , ), 204, (204, (), [ (8, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'ExecB1' , 'str' , 'val' , ), 205, (205, (), [ (8, 1, None, None) , 
			 (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'ExecB2' , 'str' , 'val' , ), 206, (206, (), [ (8, 1, None, None) , 
			 (8209, 1, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'ExecB3' , 'str' , ), 207, (207, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'ExecC' , 'str' , 'val' , 'pRet' , ), 208, (208, (), [ 
			 (8, 1, None, None) , (3, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'ExecC1' , 'str' , 'val1' , 'pRet' , ), 209, (209, (), [ 
			 (8, 1, None, None) , (3, 1, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'ExecC2' , 'val' , 'str' , 'str1' , ), 210, (210, (), [ 
			 (3, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'ExecC3' , 'str' , 'str1' , 'str2' , 'val' , 
			 ), 211, (211, (), [ (8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'ExecC4' , 'val' , 'str' , 'pStr2' , 'pRet' , 
			 ), 212, (212, (), [ (3, 1, None, None) , (8, 1, None, None) , (16392, 2, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'ExecC5' , ), 213, (213, (), [ ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
]

z_v11_0_IController_vtables_dispatch_ = 1
z_v11_0_IController_vtables_ = [
	(( 'IE' , 'pRet' , ), 100, (100, (), [ (16393, 10, None, "IID('{9F8FEB96-0027-45A8-AC7F-25F1A558F85E}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Firefox' , 'pRet' , ), 101, (101, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'OpenLog' , 'FileName' , 'pRet' , ), 102, (102, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{53BD74EF-9E8B-4575-A8A3-E49A5B8D27FC}')") , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Wait' , 'Plugin' , 'timeOutSecs' , 'pRet' , ), 103, (103, (), [ 
			 (9, 1, None, "IID('{F18298C2-6F2D-417B-8EFA-4A5AC4C64C9A}')") , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'IsBasicEdition' , 'pRet' , ), 104, (104, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Version' , 'pRet' , ), 105, (105, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'WaitEx' , 'Plugin' , 'timeOutSecs' , 'waitForPageLoadEvent' , 'waitForRenderStartEvent' , 
			 'httpIdleSecs' , 'pRet' , ), 106, (106, (), [ (9, 1, None, "IID('{F18298C2-6F2D-417B-8EFA-4A5AC4C64C9A}')") , (3, 1, None, None) , 
			 (11, 1, None, None) , (11, 1, None, None) , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'AttachByTitle' , 'pageTitle' , 'pRet' , ), 107, (107, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{F18298C2-6F2D-417B-8EFA-4A5AC4C64C9A}')") , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

z_v11_1_15_Chrome_vtables_dispatch_ = 1
z_v11_1_15_Chrome_vtables_ = [
	(( 'New' , 'chromeChannel' , 'pRet' , ), 1610743808, (1610743808, (), [ (8, 49, "''", None) , 
			 (16393, 10, None, "IID('{F18298C2-6F2D-417B-8EFA-4A5AC4C64C9A}')") , ], 1 , 1 , 4 , 0 , 56 , (3, 32, None, None) , 0 , )),
]

z_v8_2_Entry_vtables_dispatch_ = 1
z_v8_2_Entry_vtables_ = [
	(( 'URL' , 'pRet' , ), 100, (100, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Method' , 'pRet' , ), 101, (101, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Started' , 'pRet' , ), 102, (102, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'StartedSecs' , 'pRet' , ), 103, (103, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'StartedDateTime' , 'pRet' , ), 104, (104, (), [ (16391, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Time' , 'pRet' , ), 105, (105, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Result' , 'pRet' , ), 106, (106, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'CacheBefore' , 'pRet' , ), 107, (107, (), [ (16393, 10, None, "IID('{30108071-50D2-40B6-9107-D8300B1FA764}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'CacheAfter' , 'pRet' , ), 108, (108, (), [ (16393, 10, None, "IID('{30108071-50D2-40B6-9107-D8300B1FA764}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'ServerIP' , 'pRet' , ), 109, (109, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'ServerPort' , 'pRet' , ), 110, (110, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'ClientIP' , 'pRet' , ), 111, (111, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'ClientPort' , 'pRet' , ), 112, (112, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Request' , 'pRet' , ), 113, (113, (), [ (16393, 10, None, "IID('{F5234216-06DF-4D7A-A59A-DA4A8F2B0338}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Response' , 'pRet' , ), 114, (114, (), [ (16393, 10, None, "IID('{BEAF8831-18CF-4B1B-AD18-112C675A2443}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Content' , 'pRet' , ), 115, (115, (), [ (16393, 10, None, "IID('{E6086F4F-66DB-40DB-A8BC-11555566A6DA}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'IsRestrictedURL' , 'pRet' , ), 116, (116, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'BytesSent' , 'pRet' , ), 117, (117, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'BytesReceived' , 'pRet' , ), 118, (118, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'IsComplete' , 'pRet' , ), 119, (119, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'StatusCode' , 'pRet' , ), 120, (120, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Error' , 'pRet' , ), 121, (121, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'IsRedirect' , 'pRet' , ), 122, (122, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'RedirectURL' , 'pRet' , ), 123, (123, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Page' , 'pRet' , ), 124, (124, (), [ (16393, 10, None, "IID('{BE4A78A7-B009-4B09-A2E4-E8EA96159599}')") , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Timings' , 'pRet' , ), 125, (125, (), [ (16393, 10, None, "IID('{71F7B683-98D5-4451-B20E-2DEA1E4D22B1}')") , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Warnings' , 'pRet' , ), 126, (126, (), [ (16393, 10, None, "IID('{58A600C1-1413-4972-9A53-2CCD73FE01EC}')") , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'Comment' , 'pOut' , ), 127, (127, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Comment' , 'pOut' , ), 127, (127, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'ID' , 'pRet' , ), 128, (128, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'ConnectionID' , 'pRet' , ), 129, (129, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
]

z_v9_CacheInfo_vtables_dispatch_ = 1
z_v9_CacheInfo_vtables_ = [
	(( 'URLInCache' , 'pRet' , ), 1610743808, (1610743808, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Expires' , 'pRet' , ), 1610743809, (1610743809, (), [ (16391, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'IsExpiresSet' , 'pRet' , ), 1610743810, (1610743810, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'LastUpdate' , 'pRet' , ), 1610743811, (1610743811, (), [ (16391, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'LastAccess' , 'pRet' , ), 1610743812, (1610743812, (), [ (16391, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'LastModified' , 'pRet' , ), 1610743813, (1610743813, (), [ (16391, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'IsLastModifiedSet' , 'pRet' , ), 1610743814, (1610743814, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'ETag' , 'pRet' , ), 1610743815, (1610743815, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'HitCount' , 'pRet' , ), 1610743816, (1610743816, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
]

z_v9_Entry_vtables_dispatch_ = 1
z_v9_Entry_vtables_ = [
	(( 'URL' , 'pRet' , ), 100, (100, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Method' , 'pRet' , ), 101, (101, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Started' , 'pRet' , ), 102, (102, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'StartedSecs' , 'pRet' , ), 103, (103, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'StartedDateTime' , 'pRet' , ), 104, (104, (), [ (16391, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Time' , 'pRet' , ), 105, (105, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Result' , 'pRet' , ), 106, (106, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'CacheBefore' , 'pRet' , ), 107, (107, (), [ (16393, 10, None, "IID('{30108071-50D2-40B6-9107-D8300B1FA764}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'CacheAfter' , 'pRet' , ), 108, (108, (), [ (16393, 10, None, "IID('{30108071-50D2-40B6-9107-D8300B1FA764}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'ServerIP' , 'pRet' , ), 109, (109, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'ServerPort' , 'pRet' , ), 110, (110, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'ClientIP' , 'pRet' , ), 111, (111, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'ClientPort' , 'pRet' , ), 112, (112, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Request' , 'pRet' , ), 113, (113, (), [ (16393, 10, None, "IID('{F5234216-06DF-4D7A-A59A-DA4A8F2B0338}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Response' , 'pRet' , ), 114, (114, (), [ (16393, 10, None, "IID('{BEAF8831-18CF-4B1B-AD18-112C675A2443}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Content' , 'pRet' , ), 115, (115, (), [ (16393, 10, None, "IID('{E6086F4F-66DB-40DB-A8BC-11555566A6DA}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'IsRestrictedURL' , 'pRet' , ), 116, (116, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'BytesSent' , 'pRet' , ), 117, (117, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'BytesReceived' , 'pRet' , ), 118, (118, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'IsComplete' , 'pRet' , ), 119, (119, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'StatusCode' , 'pRet' , ), 120, (120, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Error' , 'pRet' , ), 121, (121, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'IsRedirect' , 'pRet' , ), 122, (122, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'RedirectURL' , 'pRet' , ), 123, (123, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Page' , 'pRet' , ), 124, (124, (), [ (16393, 10, None, "IID('{BE4A78A7-B009-4B09-A2E4-E8EA96159599}')") , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Timings' , 'pRet' , ), 125, (125, (), [ (16393, 10, None, "IID('{71F7B683-98D5-4451-B20E-2DEA1E4D22B1}')") , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Warnings' , 'pRet' , ), 126, (126, (), [ (16393, 10, None, "IID('{58A600C1-1413-4972-9A53-2CCD73FE01EC}')") , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'Comment' , 'pOut' , ), 127, (127, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Comment' , 'pOut' , ), 127, (127, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'ID' , 'pRet' , ), 128, (128, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'ConnectionID' , 'pRet' , ), 129, (129, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'IsSPDY' , 'pRet' , ), 130, (130, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'SPDYStreamID' , 'pRet' , ), 131, (131, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
]

z_v9_TimingSummaries_vtables_dispatch_ = 1
z_v9_TimingSummaries_vtables_ = [
	(( 'Blocked' , 'pRet' , ), 1610743808, (1610743808, (), [ (16393, 10, None, "IID('{A78CB278-109B-41B2-9971-42A90CB19315}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'DNSLookup' , 'pRet' , ), 1610743809, (1610743809, (), [ (16393, 10, None, "IID('{A78CB278-109B-41B2-9971-42A90CB19315}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Connect' , 'pRet' , ), 1610743810, (1610743810, (), [ (16393, 10, None, "IID('{A78CB278-109B-41B2-9971-42A90CB19315}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Send' , 'pRet' , ), 1610743811, (1610743811, (), [ (16393, 10, None, "IID('{A78CB278-109B-41B2-9971-42A90CB19315}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Wait' , 'pRet' , ), 1610743812, (1610743812, (), [ (16393, 10, None, "IID('{A78CB278-109B-41B2-9971-42A90CB19315}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Receive' , 'pRet' , ), 1610743813, (1610743813, (), [ (16393, 10, None, "IID('{A78CB278-109B-41B2-9971-42A90CB19315}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'TTFB' , 'pRet' , ), 1610743814, (1610743814, (), [ (16393, 10, None, "IID('{A78CB278-109B-41B2-9971-42A90CB19315}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Network' , 'pRet' , ), 1610743815, (1610743815, (), [ (16393, 10, None, "IID('{A78CB278-109B-41B2-9971-42A90CB19315}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'CacheRead' , 'pRet' , ), 1610743816, (1610743816, (), [ (16393, 10, None, "IID('{A78CB278-109B-41B2-9971-42A90CB19315}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
]

z_v9_Timings_vtables_dispatch_ = 1
z_v9_Timings_vtables_ = [
	(( 'Blocked' , 'pRet' , ), 1610743808, (1610743808, (), [ (16393, 10, None, "IID('{BBCC50D3-8A27-46C9-A457-4E4B6BF936FD}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'DNSLookup' , 'pRet' , ), 1610743809, (1610743809, (), [ (16393, 10, None, "IID('{BBCC50D3-8A27-46C9-A457-4E4B6BF936FD}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Connect' , 'pRet' , ), 1610743810, (1610743810, (), [ (16393, 10, None, "IID('{BBCC50D3-8A27-46C9-A457-4E4B6BF936FD}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Send' , 'pRet' , ), 1610743811, (1610743811, (), [ (16393, 10, None, "IID('{BBCC50D3-8A27-46C9-A457-4E4B6BF936FD}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Wait' , 'pRet' , ), 1610743812, (1610743812, (), [ (16393, 10, None, "IID('{BBCC50D3-8A27-46C9-A457-4E4B6BF936FD}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Receive' , 'pRet' , ), 1610743813, (1610743813, (), [ (16393, 10, None, "IID('{BBCC50D3-8A27-46C9-A457-4E4B6BF936FD}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'TTFB' , 'pRet' , ), 1610743814, (1610743814, (), [ (16393, 10, None, "IID('{BBCC50D3-8A27-46C9-A457-4E4B6BF936FD}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Network' , 'pRet' , ), 1610743815, (1610743815, (), [ (16393, 10, None, "IID('{BBCC50D3-8A27-46C9-A457-4E4B6BF936FD}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'CacheRead' , 'pRet' , ), 1610743816, (1610743816, (), [ (16393, 10, None, "IID('{BBCC50D3-8A27-46C9-A457-4E4B6BF936FD}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
]

RecordMap = {
}

CLSIDToClassMap = {
	'{BE4A78A7-B009-4B09-A2E4-E8EA96159599}' : Page,
	'{33F42185-77A9-4B0B-833F-2BA039017CBA}' : Entries,
	'{F00EDAEF-92F9-4921-BFB2-3BE1FCBE8E66}' : Entry,
	'{30108071-50D2-40B6-9107-D8300B1FA764}' : CacheInfo,
	'{F5234216-06DF-4D7A-A59A-DA4A8F2B0338}' : Request,
	'{E8BB54CB-32C4-4E31-BD02-FFF4670201DB}' : Cookies,
	'{0285A8EF-8290-4BCD-9482-7BE19A86136D}' : Cookie,
	'{F9F5CDCD-245F-4666-AD51-B742D1F7296E}' : Headers,
	'{E4B992AF-8CE5-4B3B-8697-EE31916D8DB4}' : Header,
	'{6C1B38A6-9F2C-4DC5-BEFA-629964C5B7F0}' : POSTParameters,
	'{A065DFB9-32D5-419D-BADB-0BEF567C7C2A}' : POSTParameter,
	'{63A3AEC9-5645-4E59-91DE-6F1E6FFE6B01}' : QueryStringValues,
	'{CE39DFFD-65FF-4B1A-B38D-541D3ECBDBEC}' : QueryStringValue,
	'{BEAF8831-18CF-4B1B-AD18-112C675A2443}' : Response,
	'{E6086F4F-66DB-40DB-A8BC-11555566A6DA}' : Content,
	'{71F7B683-98D5-4451-B20E-2DEA1E4D22B1}' : Timings,
	'{BBCC50D3-8A27-46C9-A457-4E4B6BF936FD}' : Timing,
	'{58A600C1-1413-4972-9A53-2CCD73FE01EC}' : Warnings,
	'{B7A07AA1-F28C-4616-A1E2-6DA53AB39752}' : Warning,
	'{8340029F-30FB-458B-98E2-A9641DC5D0AB}' : Summary,
	'{73A9B44B-0FB6-44F9-BB8A-370EBFC7BF98}' : ResultSummaries,
	'{237800E5-58C3-4A42-BA42-E84FAEA906AE}' : ResultSummary,
	'{5EC931D6-6F2D-456E-BE4F-0CF7E0A4A9A3}' : TimingSummaries,
	'{A78CB278-109B-41B2-9971-42A90CB19315}' : TimingSummary,
	'{FB58D46D-06BA-4EDC-AE0A-F0071A1F52FD}' : WarningSummaries,
	'{77D55250-8974-4C9D-B452-FA611225CC6B}' : WarningSummary,
	'{5422D39D-A1DD-40EF-A4C2-C36C101D693B}' : PageEvents,
	'{57602A1E-6929-476F-9CB8-1461432337F3}' : PageEvent,
	'{00794C37-D4E1-44D1-9B21-8247A473E061}' : z_v9_CacheInfo,
	'{22E95B79-EAD5-4432-9F2E-05D6F630074F}' : z_v9_Timings,
	'{7C121585-EECF-4EB1-9DB0-50D0BB3EE82F}' : z_v9_TimingSummaries,
	'{C972CF14-E223-48E0-9D25-2BCF1550A74C}' : z_v9_Entry,
	'{6BA71A40-892E-4031-9252-BFEB02E340D9}' : z_v8_2_Entry,
	'{26B8534B-59E5-4537-AD52-8AB021EDFE34}' : Pages,
	'{53BD74EF-9E8B-4575-A8A3-E49A5B8D27FC}' : Log,
	'{F18298C2-6F2D-417B-8EFA-4A5AC4C64C9A}' : Plugin,
	'{9F8FEB96-0027-45A8-AC7F-25F1A558F85E}' : IE,
	'{599C06FF-EECA-409D-AC55-B6927E6D6886}' : z_v11_1_15_Chrome,
	'{09609DDF-174B-478F-A403-DFC01D82F2C3}' : Chrome,
	'{F3638BC8-748C-49D7-9E84-B1C3AFCDBFF8}' : IController,
	'{9EF1CD3C-EFBD-402A-98BF-D9FB9AF510FA}' : z_v11_0_IController,
	'{8BF52022-A0AF-4EA5-A6EB-ABC0D0F2484F}' : _IReserved2,
	'{CF8B3C81-4F3E-4CBA-ADE6-8CD2C3E778D8}' : _IReserved3,
	'{C4CEDB78-2B64-4703-99BE-A037A849D703}' : Controller,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
	'{BE4A78A7-B009-4B09-A2E4-E8EA96159599}' : 'Page',
	'{33F42185-77A9-4B0B-833F-2BA039017CBA}' : 'Entries',
	'{F00EDAEF-92F9-4921-BFB2-3BE1FCBE8E66}' : 'Entry',
	'{30108071-50D2-40B6-9107-D8300B1FA764}' : 'CacheInfo',
	'{F5234216-06DF-4D7A-A59A-DA4A8F2B0338}' : 'Request',
	'{E8BB54CB-32C4-4E31-BD02-FFF4670201DB}' : 'Cookies',
	'{0285A8EF-8290-4BCD-9482-7BE19A86136D}' : 'Cookie',
	'{F9F5CDCD-245F-4666-AD51-B742D1F7296E}' : 'Headers',
	'{E4B992AF-8CE5-4B3B-8697-EE31916D8DB4}' : 'Header',
	'{6C1B38A6-9F2C-4DC5-BEFA-629964C5B7F0}' : 'POSTParameters',
	'{A065DFB9-32D5-419D-BADB-0BEF567C7C2A}' : 'POSTParameter',
	'{63A3AEC9-5645-4E59-91DE-6F1E6FFE6B01}' : 'QueryStringValues',
	'{CE39DFFD-65FF-4B1A-B38D-541D3ECBDBEC}' : 'QueryStringValue',
	'{BEAF8831-18CF-4B1B-AD18-112C675A2443}' : 'Response',
	'{E6086F4F-66DB-40DB-A8BC-11555566A6DA}' : 'Content',
	'{71F7B683-98D5-4451-B20E-2DEA1E4D22B1}' : 'Timings',
	'{BBCC50D3-8A27-46C9-A457-4E4B6BF936FD}' : 'Timing',
	'{58A600C1-1413-4972-9A53-2CCD73FE01EC}' : 'Warnings',
	'{B7A07AA1-F28C-4616-A1E2-6DA53AB39752}' : 'Warning',
	'{8340029F-30FB-458B-98E2-A9641DC5D0AB}' : 'Summary',
	'{73A9B44B-0FB6-44F9-BB8A-370EBFC7BF98}' : 'ResultSummaries',
	'{237800E5-58C3-4A42-BA42-E84FAEA906AE}' : 'ResultSummary',
	'{5EC931D6-6F2D-456E-BE4F-0CF7E0A4A9A3}' : 'TimingSummaries',
	'{A78CB278-109B-41B2-9971-42A90CB19315}' : 'TimingSummary',
	'{FB58D46D-06BA-4EDC-AE0A-F0071A1F52FD}' : 'WarningSummaries',
	'{77D55250-8974-4C9D-B452-FA611225CC6B}' : 'WarningSummary',
	'{5422D39D-A1DD-40EF-A4C2-C36C101D693B}' : 'PageEvents',
	'{57602A1E-6929-476F-9CB8-1461432337F3}' : 'PageEvent',
	'{00794C37-D4E1-44D1-9B21-8247A473E061}' : 'z_v9_CacheInfo',
	'{22E95B79-EAD5-4432-9F2E-05D6F630074F}' : 'z_v9_Timings',
	'{7C121585-EECF-4EB1-9DB0-50D0BB3EE82F}' : 'z_v9_TimingSummaries',
	'{C972CF14-E223-48E0-9D25-2BCF1550A74C}' : 'z_v9_Entry',
	'{6BA71A40-892E-4031-9252-BFEB02E340D9}' : 'z_v8_2_Entry',
	'{26B8534B-59E5-4537-AD52-8AB021EDFE34}' : 'Pages',
	'{53BD74EF-9E8B-4575-A8A3-E49A5B8D27FC}' : 'Log',
	'{F18298C2-6F2D-417B-8EFA-4A5AC4C64C9A}' : 'Plugin',
	'{9F8FEB96-0027-45A8-AC7F-25F1A558F85E}' : 'IE',
	'{599C06FF-EECA-409D-AC55-B6927E6D6886}' : 'z_v11_1_15_Chrome',
	'{09609DDF-174B-478F-A403-DFC01D82F2C3}' : 'Chrome',
	'{F3638BC8-748C-49D7-9E84-B1C3AFCDBFF8}' : 'IController',
	'{9EF1CD3C-EFBD-402A-98BF-D9FB9AF510FA}' : 'z_v11_0_IController',
	'{8BF52022-A0AF-4EA5-A6EB-ABC0D0F2484F}' : '_IReserved2',
	'{CF8B3C81-4F3E-4CBA-ADE6-8CD2C3E778D8}' : '_IReserved3',
}


NamesToIIDMap = {
	'Page' : '{BE4A78A7-B009-4B09-A2E4-E8EA96159599}',
	'Entries' : '{33F42185-77A9-4B0B-833F-2BA039017CBA}',
	'Entry' : '{F00EDAEF-92F9-4921-BFB2-3BE1FCBE8E66}',
	'CacheInfo' : '{30108071-50D2-40B6-9107-D8300B1FA764}',
	'Request' : '{F5234216-06DF-4D7A-A59A-DA4A8F2B0338}',
	'Cookies' : '{E8BB54CB-32C4-4E31-BD02-FFF4670201DB}',
	'Cookie' : '{0285A8EF-8290-4BCD-9482-7BE19A86136D}',
	'Headers' : '{F9F5CDCD-245F-4666-AD51-B742D1F7296E}',
	'Header' : '{E4B992AF-8CE5-4B3B-8697-EE31916D8DB4}',
	'POSTParameters' : '{6C1B38A6-9F2C-4DC5-BEFA-629964C5B7F0}',
	'POSTParameter' : '{A065DFB9-32D5-419D-BADB-0BEF567C7C2A}',
	'QueryStringValues' : '{63A3AEC9-5645-4E59-91DE-6F1E6FFE6B01}',
	'QueryStringValue' : '{CE39DFFD-65FF-4B1A-B38D-541D3ECBDBEC}',
	'Response' : '{BEAF8831-18CF-4B1B-AD18-112C675A2443}',
	'Content' : '{E6086F4F-66DB-40DB-A8BC-11555566A6DA}',
	'Timings' : '{71F7B683-98D5-4451-B20E-2DEA1E4D22B1}',
	'Timing' : '{BBCC50D3-8A27-46C9-A457-4E4B6BF936FD}',
	'Warnings' : '{58A600C1-1413-4972-9A53-2CCD73FE01EC}',
	'Warning' : '{B7A07AA1-F28C-4616-A1E2-6DA53AB39752}',
	'Summary' : '{8340029F-30FB-458B-98E2-A9641DC5D0AB}',
	'ResultSummaries' : '{73A9B44B-0FB6-44F9-BB8A-370EBFC7BF98}',
	'ResultSummary' : '{237800E5-58C3-4A42-BA42-E84FAEA906AE}',
	'TimingSummaries' : '{5EC931D6-6F2D-456E-BE4F-0CF7E0A4A9A3}',
	'TimingSummary' : '{A78CB278-109B-41B2-9971-42A90CB19315}',
	'WarningSummaries' : '{FB58D46D-06BA-4EDC-AE0A-F0071A1F52FD}',
	'WarningSummary' : '{77D55250-8974-4C9D-B452-FA611225CC6B}',
	'PageEvents' : '{5422D39D-A1DD-40EF-A4C2-C36C101D693B}',
	'PageEvent' : '{57602A1E-6929-476F-9CB8-1461432337F3}',
	'z_v9_CacheInfo' : '{00794C37-D4E1-44D1-9B21-8247A473E061}',
	'z_v9_Timings' : '{22E95B79-EAD5-4432-9F2E-05D6F630074F}',
	'z_v9_TimingSummaries' : '{7C121585-EECF-4EB1-9DB0-50D0BB3EE82F}',
	'z_v9_Entry' : '{C972CF14-E223-48E0-9D25-2BCF1550A74C}',
	'z_v8_2_Entry' : '{6BA71A40-892E-4031-9252-BFEB02E340D9}',
	'Pages' : '{26B8534B-59E5-4537-AD52-8AB021EDFE34}',
	'Log' : '{53BD74EF-9E8B-4575-A8A3-E49A5B8D27FC}',
	'Plugin' : '{F18298C2-6F2D-417B-8EFA-4A5AC4C64C9A}',
	'IE' : '{9F8FEB96-0027-45A8-AC7F-25F1A558F85E}',
	'z_v11_1_15_Chrome' : '{599C06FF-EECA-409D-AC55-B6927E6D6886}',
	'Chrome' : '{09609DDF-174B-478F-A403-DFC01D82F2C3}',
	'IController' : '{F3638BC8-748C-49D7-9E84-B1C3AFCDBFF8}',
	'z_v11_0_IController' : '{9EF1CD3C-EFBD-402A-98BF-D9FB9AF510FA}',
	'_IReserved2' : '{8BF52022-A0AF-4EA5-A6EB-ABC0D0F2484F}',
	'_IReserved3' : '{CF8B3C81-4F3E-4CBA-ADE6-8CD2C3E778D8}',
}


