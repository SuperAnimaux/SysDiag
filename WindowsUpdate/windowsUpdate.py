import win32com.client

# Créer une instance du client Windows Update API
update_session = win32com.client.Dispatch('Microsoft.Update.Session')

# Obtenir les mises à jour disponibles
searcher = update_session.CreateUpdateSearcher()
search_result = searcher.Search('IsInstalled=0')  # Recherche des mises à jour non installées

print(f"Mises à jour disponibles : {search_result.Updates.Count}")
for update in search_result.Updates:
    print(f"Nom de la mise à jour : {update.Title}")
    print(f"Description : {update.Description}")
    print("-" * 50)