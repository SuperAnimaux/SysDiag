from Evtx import Evtx
import os

LOGS_PATH = r"C:\Windows\System32\winevt\Logs"

def list_evtx_files(LOGS_PATH):
    """Retourne la liste des fichiers journaux (.evtx)"""
    return [os.path.join(LOGS_PATH, f) for f in os.listdir(LOGS_PATH) if f.endswith(".evtx")]

def check_evtx_integrity(file_path):
    """Vérifie si un journal Windows est corrompu"""
    try:
        with Evtx.Evtx(file_path) as log:
            for i, record in enumerate(log.records()):
                if i >= 10:
                    break
                _ = record.xml()
        return True
    except Exception as e:
        print(f"Erreur lors de la lecture de {file_path} : {e}")
        return False


def check_all_evtx(file_paths_list):
    for file_path in file_paths_list:
        if check_evtx_integrity(file_path) is True:
            print(f"{file_path} : OK\n-------------------------------------")
        else:
            print(f"{file_path} : NOT OK\n-------------------------------------")


def show_list(LOGS_PATH_LIST):
    for LOGS_PATH in LOGS_PATH_LIST:
        print(f"{LOGS_PATH}\n---------------------------------------------")
