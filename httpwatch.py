import httpwatch_automation as HttpWatch
import win32com.client


controller: HttpWatch.IController = win32com.client.Dispatch(HttpWatch.Controller.CLSID)

# Create a new instance of HttpWatch in Chrome
# (Change to controller.IE.New() to open Internet Explorer instead)
plugin = controller.Chrome.New()

# Start Recording HTTP/HTTPS traffic
plugin.Log.EnableFilter(False)
plugin.Record()

# Goto to the URL and wait for the page to be loaded
url = "https://www.facebook.com"
plugin.GotoURL(url)
print("\nWaiting for page to finish loading...")
controller.Wait(plugin, -1)

print("Page loading complete")

# Stop recording HTTP/HTTPS
plugin.Stop()

if plugin.Log.Pages.Count != 0:
    print("\nPage Title: '" + plugin.Log.Pages(0).Title + "'")

    # Display summary statistics for page
    summary = plugin.Log.Pages(0).Entries.Summary
    print( "Total time to load page (secs):      " + str(summary.Time))
    print( "Number of bytes received on network: " + str(summary.BytesReceived))
    print( "HTTP compression saving (bytes):     " + str(summary.CompressionSavedBytes))
    print( "Number of round trips:               " + str(summary.RoundTrips))
    print( "Number of errors:                    " + str(summary.Errors.Count))

# Close down Chrome
plugin.CloseBrowser()