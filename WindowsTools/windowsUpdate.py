import win32com.client


def checkUpdates():
    try:
        update_session = win32com.client.Dispatch('Microsoft.Update.Session')


        searcher = update_session.CreateUpdateSearcher()
        search_result = searcher.Search('IsInstalled=0')

        print(f"Updates available: {search_result.Updates.Count}")
        for update in search_result.Updates:
            print(f"Update name : {update.Title}")
            print(f"Description : {update.Description}")
            print("-" * 50)

    except Exception as e:
        print(f"An error has occurred : {e}")