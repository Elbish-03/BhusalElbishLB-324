# LB 324

## Aufgabe 2

Erklären Sie hier, wie man `pre-commit` installiert.

Schritt 1: Einrichten von pre-commit

Falls pre-commit noch nicht auf dem lokalen Entwicklungssystem installiert ist, kann es mit dem folgenden Befehl installiert werden (vorausgesetzt, Python ist auf dem System installiert):

Code: pip install pre-commit

Schritt 2: Konfiguration der .pre-commit-config.yaml-Datei

Die Benutzer müssen sicherstellen, dass eine .pre-commit-config.yaml-Datei im Stammverzeichnis ihres Projekts vorhanden ist und die erforderlichen Hooks und Tools für Tests und Codeformatierung enthält. Sie können die vorher bereitgestellte Konfiguration verwenden und an ihre Projektanforderungen anpassen.

Schritt 3: Installation der Hooks

Nachdem die .pre-commit-config.yaml-Datei konfiguriert ist, führen die Benutzer im Projektverzeichnis den folgenden Befehl aus, um die in der Konfigurationsdatei definierten Hooks zu installieren:

Code: pre-commit install

Schritt 4: Verwendung der Automatisierungen

Die Benutzer müssen keine zusätzlichen Befehle ausführen. Sobald sie Änderungen committen oder pushen, werden die vordefinierten Hooks automatisch ausgeführt:

Push (Änderungen auf den Server übertragen): Der Code wird vor dem Push automatisch getestet.

Commit (lokale Änderungen committen): Der Code wird vor dem Commit automatisch formatiert.

Es sind keine manuellen Schritte erforderlich, da die Automatisierungen automatisch im Hintergrund ausgeführt werden.

## Aufgabe 4

Erklären Sie hier, wie Sie das Passwort aus Ihrer lokalen `.env` auf Azure übertragen.

Default domain
bhusalelbishtagesbuch.azurewebsites.net

#Nötige Schritte um das geheime Passwort in Azure zu übertragen

Zugriff auf das Azure-Portal: Öffnen Sie einen Webbrowser und gehen Sie zur Azure-Portal-Website. Melden Sie sich mit Ihrem Azure-Konto an.

Suchen Sie die Azure App Service-Instanz: Suchen Sie in der Azure-Portal-Oberfläche nach Ihrer Azure App Service-Instanz, auf der Ihre Anwendung gehostet ist.

Konfigurieren der Umgebungsvariablen: Navigieren Sie zu den Einstellungen Ihrer App Service-Instanz. In den Einstellungen finden Sie normalerweise einen Bereich mit dem Namen "Konfiguration" oder "Anwendungseinstellungen". Dies ist der richtige Ort, um Umgebungsvariablen festzulegen.

Hinzufügen einer neuen Umgebungsvariable: Innerhalb der Konfiguration können Sie eine neue Umgebungsvariable erstellen. Geben Sie einen Namen für die Umgebungsvariable ein, z. B. "SECRET_PASSWORD", und fügen Sie den Wert ein, der dem geheimen Passwort in Ihrer .env-Datei entspricht.

Speichern der Änderungen: Nachdem Sie den Namen und den Wert eingegeben haben, speichern Sie die Änderungen. Dadurch wird die Umgebungsvariable in Ihrer Azure-App Service-Instanz konfiguriert.

Neustart Ihrer Anwendung: Um sicherzustellen, dass Ihre Anwendung die neuen Umgebungsvariablen verwendet, starten Sie Ihre Anwendung neu. Dies gewährleistet, dass die Änderungen wirksam werden.

#Stellen Sie sicher, dass der Name der Umgebungsvariable in Ihrer Azure-Konfiguration genau mit dem in Ihrer .env-Datei übereinstimmt. Jede Abweichung im Namen kann dazu führen, dass die Umgebungsvariable nicht erkannt wird und Ihre Anwendung möglicherweise nicht ordnungsgemäß funktioniert.
