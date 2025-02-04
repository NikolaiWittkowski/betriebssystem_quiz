import random

class GrundbegriffeBetriebssystem:
    questions = [
        ("Was ist ein Betriebssystem?",
         "Schnittstelle zwischen Hardware und Benutzer",
         "Ein spezielles Computergehäuse",
         "Eine bestimmte Computeranwendung",
         "Ein Netzwerkprotokoll"),

        ("Welche Hauptaufgaben hat ein Betriebssystem?",
         "Ressourcenmanagement und Kontrolle & Schutz",
         "Nur Hardwaresteuerung",
         "Nur Prozessverwaltung",
         "Nur Dateisysteme verwalten"),

        ("Was beschreibt Zuverlässigkeit als Qualität eines Betriebssystems?",
         "Stabilität gegen Fehler und keine globalen Abstürze",
         "Hohe CPU-Auslastung",
         "Hohe Speicherauslastung",
         "Benutzerfreundlichkeit"),

        ("Was ist der Kernel in einem Betriebssystem?",
         "Das Programm, das dauerhaft läuft und grundlegende Funktionen bereitstellt",
         "Ein Speicherverwaltungsprozess",
         "Ein Netzwerkprotokoll",
         "Ein Hardwaretreiber"),

        ("Was ist ein Hauptvorteil der Modularität eines Betriebssystems?",
         "Leicht zu warten und erweiterbar",
         "Hohe CPU-Auslastung",
         "Hohe Speicherauslastung",
         "Benutzerfreundlichkeit"),

        ("Welche Aufgabe hat die Prozessverwaltung im Betriebssystem?",
         "Erzeugung, Synchronisation & Beendigung von Prozessen",
         "Nur Hardwaresteuerung",
         "Nur Verwaltung von Dateisystemen",
         "Nur Verwaltung von Speicher"),

        ("Was ist der primäre Unterschied zwischen Primärspeicher und Sekundärspeicher?",
         "Primärspeicher ist direkt von der CPU zugänglich, Sekundärspeicher ist langsamer",
         "Primärspeicher ist langsamer, Sekundärspeicher ist direkt von der CPU zugänglich",
         "Beide sind gleich schnell",
         "Primärspeicher ist nur für Archivierung gedacht"),

        ("Welche Eigenschaft beschreibt die Portabilität eines Betriebssystems?",
         "Anpassbar auf verschiedene Hardware",
         "Nur für bestimmte Hardware geeignet",
         "Hohe CPU-Auslastung",
         "Hohe Speicherauslastung"),

        ("Welche Dienste stellt ein Betriebssystem bereit?",
         "Prozessverwaltung, Speicherverwaltung, Dateisysteme, E/A-Verwaltung",
         "Nur Hardwaresteuerung",
         "Nur Netzwerkdienste",
         "Nur Benutzerschnittstellen"),

        ("Was ist ein Beispiel für einen Tertiärspeicher?",
         "Magnetbänder",
         "RAM",
         "SSD",
         "Festplatte"),

        ("Welche Hauptkomponenten bestehen in einem Computersystem?",
         "Hardware, Betriebssystem, Anwendungsprogramme, Benutzer",
         "Nur Hardware und Benutzer",
         "Nur Betriebssystem und Anwendungsprogramme",
         "Nur Hardware und Anwendungsprogramme"),

        ("Was ist das Ziel von Ressourcenmanagement im Betriebssystem?",
         "Verwaltung von CPU, Speicher, Geräten & Prozessen",
         "Nur Verwaltung von Dateisystemen",
         "Nur Benutzersteuerung",
         "Nur Verwaltung von Netzwerkdiensten"),

        ("Was ist die Definition eines Betriebssystems laut DIN 44300?",
         "Programme eines digitalen Rechensystems, die zusammen mit der Hardware die Grundlage der Betriebsarten bilden und Programme steuern & überwachen",
         "Nur Hardwaresteuerung",
         "Nur ein Betriebssystem für Server",
         "Ein Netzwerkprotokoll"),

        ("Welche Eigenschaft beschreibt Effizienz in einem Betriebssystem?",
         "Niedrige CPU- & Speicherbelastung, gute Hardware-Nutzung",
         "Hohe CPU-Auslastung",
         "Hohe Speicherauslastung",
         "Nur Benutzerfreundlichkeit"),

        ("Was verhindert Kontrolle & Schutz im Betriebssystem?",
         "Fehlverhalten & Abstürze",
         "Nur Fehlermeldungen",
         "Nur Speichermangel",
         "Nur Benutzerzugriffe"),

        ("Welche Speicherarten gibt es in der Speicherhierarchie?",
         "Primärspeicher, Sekundärspeicher, Tertiärspeicher",
         "Nur Primärspeicher und Sekundärspeicher",
         "Nur Sekundärspeicher und Tertiärspeicher",
         "Nur Primärspeicher und Tertiärspeicher"),

        ("Was ist eine zentrale Aufgabe des Betriebssystems in Bezug auf E/A-Verwaltung?",
         "Steuerung von Ein- und Ausgabegeräten",
         "Nur Benutzersteuerung",
         "Nur Prozessverwaltung",
         "Nur Dateiverwaltung"),

        ("Welche Art von Software ist ein Betriebssystem?",
         "Systemsoftware",
         "Anwendungssoftware",
         "Firmware",
         "Treiber"),

        ("Was beschreibt die Modularität eines Betriebssystems?",
         "Leicht zu warten und erweiterbar",
         "Hohe CPU-Auslastung",
         "Hohe Speicherauslastung",
         "Nur Benutzerfreundlichkeit"),

        ("Was sind die vier Hauptkomponenten eines Computersystems?",
         "Hardware, Betriebssystem, Anwendungsprogramme, Benutzer",
         "Nur Hardware und Benutzer",
         "Nur Betriebssystem und Anwendungsprogramme",
         "Nur Hardware und Anwendungsprogramme"),
    ]

class AufbauBetriebssysteme:
    questions = [
        ("Was ist ein Batch Processing?",
         "Automatische Abarbeitung von Befehlen ohne direkte Interaktion",
         "Eine visuelle Steuerung über Maus/Tastatur",
         "Eine Texteingabe über Terminal",
         "Ein GUI-Feature"),

        ("Welche Architekturtypen von Betriebssystemen gibt es?",
         "Monolithisch, Mikrokernel, Hybrid (Makrokernel)",
         "Nur Monolithisch und Mikrokernel",
         "Nur Hybrid (Makrokernel)",
         "Nur Mikrokernel und Monolithisch"),

        ("Was sind System Calls?",
         "Spezielle Funktionen für Betriebssystemnutzung",
         "Speicherverwaltungsprozesse",
         "Grafische Benutzeroberflächen",
         "Dateiverwaltungstools"),

        ("Was ist eine Benutzeroberfläche (User Interface, UI)?",
         "Eine Schnittstelle, die dem Benutzer den Zugriff auf das System ermöglicht",
         "Ein Netzwerkprotokoll",
         "Eine Speicherverwaltungsmethode",
         "Ein Betriebssystemkern"),

        ("Was ist eine GUI (Graphical User Interface)?",
         "Eine visuelle Steuerung über Maus/Tastatur",
         "Eine Texteingabe über Terminal",
         "Ein Batch Processing System",
         "Ein Netzwerkdienst"),

        ("Was ist eine CLI (Command Line Interface)?",
         "Texteingabe über Terminal",
         "Visuelle Steuerung über Maus/Tastatur",
         "Automatische Abarbeitung von Befehlen",
         "Speicherverwaltung"),

        ("Was ist ein Beispiel für ein Dateisystem?",
         "NTFS, FAT32, ext4",
         "TCP/IP",
         "SMTP",
         "HTTP"),

        ("Welche Aufgabe hat die E/A-Verwaltung?",
         "Verwaltung von Peripheriegeräten wie Tastatur, Maus, Drucker",
         "Nur Prozessverwaltung",
         "Nur Benutzersteuerung",
         "Nur Netzwerkdienste"),

        ("Was ist der Vorteil einer Mikrokernel-Architektur?",
         "Stabilität und Modularität",
         "Hohe Geschwindigkeit durch weniger Kontextwechsel",
         "Einfache Verwaltung",
         "Nur geeignet für einfache Betriebssysteme"),

        ("Welche Aufgabe hat die Speicherverwaltung im Betriebssystem?",
         "Verwaltung von Arbeitsspeicher, Dateien und Dateisystemen",
         "Nur Hardwaresteuerung",
         "Nur Verwaltung von Netzwerkdiensten",
         "Nur Benutzersteuerung"),

        ("Was ist ein Fehlerbehandlungsmechanismus im Betriebssystem?",
         "Überwachung von Hard- und Softwarefehlern",
         "Verwaltung von Netzwerkprotokollen",
         "Benutzeroberfläche",
         "Speicherverwaltung"),

        ("Welche Eigenschaft beschreibt ein monolithisches Betriebssystem?",
         "Ein einziges großes Programm mit allen Funktionen integriert",
         "Nur essenzielle Funktionen im Kernel",
         "Mischung aus Monolith und Mikrokernel",
         "Ein Speicherverwaltungssystem"),

        ("Was ist der Vorteil eines Hybrid-Betriebssystems?",
         "Balance zwischen Stabilität und Performance",
         "Nur geeignet für einfache Betriebssysteme",
         "Schlechte Performance",
         "Hohe Unsicherheit"),

        ("Welche Architekturtypen von Betriebssystemen gibt es?",
         "Monolithisch, Mikrokernel, Hybrid (Makrokernel)",
         "Nur Monolithisch und Mikrokernel",
         "Nur Hybrid (Makrokernel)",
         "Nur Mikrokernel und Monolithisch"),

        ("Welche Aufgabe hat die Programmverwaltung im Betriebssystem?",
         "Laden, Starten und Verwalten von Programmen",
         "Nur Hardwaresteuerung",
         "Nur Verwaltung von Dateisystemen",
         "Nur Netzwerkdienste"),

        ("Was ist die Aufgabe der Prozessverwaltung im Betriebssystem?",
         "Erzeugung, Synchronisation & Beendigung von Prozessen",
         "Nur Hardwaresteuerung",
         "Nur Verwaltung von Dateisystemen",
         "Nur Verwaltung von Speicher"),

        ("Welche Architekturtypen von Betriebssystemen gibt es?",
         "Monolithisch, Mikrokernel, Hybrid (Makrokernel)",
         "Nur Monolithisch und Mikrokernel",
         "Nur Hybrid (Makrokernel)",
         "Nur Mikrokernel und Monolithisch"),

        ("Was ist der Hauptvorteil einer mikrokernelbasierten Architektur?",
         "Stabilität und Modularität",
         "Hohe Geschwindigkeit durch weniger Kontextwechsel",
         "Einfachheit",
         "Komplexität"),

        ("Welche Architekturtypen von Betriebssystemen gibt es?",
         "Monolithisch, Mikrokernel, Hybrid (Makrokernel)",
         "Nur Monolithisch und Mikrokernel",
         "Nur Hybrid (Makrokernel)",
         "Nur Mikrokernel und Monolithisch"),
    ]

class UnixShell:
    questions = [
        ("Was ist die Shell?",
         "Ein Kommando-Prozessor, der Befehle ausführt",
         "Ein grafisches Benutzerinterface",
         "Ein Speicherverwaltungsprozess",
         "Ein Netzwerkdienst"),

        ("Welche Haupttypen von Shells gibt es?",
         "CLI, GUI, Batch Processing",
         "CLI, TUI, GUI",
         "GUI, CLI, Text Editor",
         "Batch Processing, CLI, TUI"),

        ("Was ist die Bourne Shell (sh)?",
         "Die erste Unix-Shell, sehr stabil",
         "Eine erweiterte Version der Korn-Shell",
         "Ein grafisches Benutzerinterface",
         "Ein Speicherverwaltungsprozess"),

        ("Was ist die Bash (Bourne Again Shell)?",
         "Die Standard-Shell auf den meisten Linux-Systemen",
         "Eine erweiterte Version der C-Shell",
         "Ein grafisches Benutzerinterface",
         "Ein Netzwerkdienst"),

        ("Was ist die Korn-Shell (ksh)?",
         "Eine Erweiterung der Bourne-Shell mit zusätzlichen Features",
         "Die erste Unix-Shell, sehr stabil",
         "Ein grafisches Benutzerinterface",
         "Ein Speicherverwaltungsprozess"),

        ("Was ist die C-Shell (csh)?",
         "Eine Shell, die an die C-Syntax angelehnt ist",
         "Eine Erweiterung der Korn-Shell",
         "Ein grafisches Benutzerinterface",
         "Ein Netzwerkdienst"),

        ("Was ist die Tcsh (TENEX C Shell)?",
         "Eine Erweiterung der C-Shell mit Autovervollständigung",
         "Die erste Unix-Shell, sehr stabil",
         "Ein grafisches Benutzerinterface",
         "Ein Speicherverwaltungsprozess"),

        ("Wie löscht man alle Dateien, die mit 'A' beginnen?",
         "Mit dem Befehl rm A*",
         "Mit dem Befehl delete A*",
         "Mit dem Befehl remove A*",
         "Mit dem Befehl erase A*"),

        ("Was ist ein Shell-Skript?",
         "Eine Datei, die eine Reihe von Shell-Befehlen enthält",
         "Ein grafisches Benutzerinterface",
         "Ein Netzwerkdienst",
         "Ein Speicherverwaltungsprozess"),

        ("Wie kopiert man eine Datei mit der Shell?",
         "Mit dem Befehl cp",
         "Mit dem Befehl copy",
         "Mit dem Befehl duplicate",
         "Mit dem Befehl clone"),

        ("Welche Shell verwendet die meisten Linux-Systeme standardmäßig?",
         "Bash (Bourne Again Shell)",
         "C-Shell (csh)",
         "Korn-Shell (ksh)",
         "Tcsh (TENEX C Shell)"),

        ("Was ist der Unterschied zwischen CLI und GUI?",
         "CLI nutzt Texteingabe über Terminal, GUI nutzt visuelle Steuerung über Maus/Tastatur",
         "CLI ist schneller als GUI",
         "CLI ist grafischer als GUI",
         "Es gibt keinen Unterschied"),

        ("Was ist Batch Processing?",
         "Automatische Abarbeitung von Befehlen ohne direkte Interaktion",
         "Eine visuelle Steuerung über Maus/Tastatur",
         "Eine Texteingabe über Terminal",
         "Ein grafisches Benutzerinterface"),

        ("Wie erstellt man einen neuen Ordner in der Shell?",
         "Mit dem Befehl mkdir",
         "Mit dem Befehl newdir",
         "Mit dem Befehl createfolder",
         "Mit dem Befehl makedir"),

        ("Was macht der Befehl ls in der Shell?",
         "Listet Dateien und Verzeichnisse auf",
         "Kopiert Dateien und Verzeichnisse",
         "Löscht Dateien und Verzeichnisse",
         "Erstellt neue Dateien und Verzeichnisse"),

        ("Wie ändert man das aktuelle Verzeichnis in der Shell?",
         "Mit dem Befehl cd",
         "Mit dem Befehl change",
         "Mit dem Befehl goto",
         "Mit dem Befehl dir"),

        ("Was macht der Befehl pwd in der Shell?",
         "Zeigt den aktuellen Verzeichnispfad an",
         "Wechselt das aktuelle Verzeichnis",
         "Löscht das aktuelle Verzeichnis",
         "Kopiert das aktuelle Verzeichnis"),

        ("Wie zeigt man den Inhalt einer Datei in der Shell an?",
         "Mit dem Befehl cat",
         "Mit dem Befehl show",
         "Mit dem Befehl view",
         "Mit dem Befehl display"),

        ("Wie löscht man eine Datei in der Shell?",
         "Mit dem Befehl rm",
         "Mit dem Befehl delete",
         "Mit dem Befehl remove",
         "Mit dem Befehl erase"),

        ("Was ist eine Umgebungsvariable in der Shell?",
         "Eine Variable, die das Verhalten der Shell steuert",
         "Eine Datei im aktuellen Verzeichnis",
         "Ein Verzeichnis auf dem Dateisystem",
         "Ein grafisches Benutzerinterface"),
    ]

class GrossrechnerMainframes:
    questions = [
        ("Was sind Großrechner (Mainframes)?",
         "Leistungsstarke Zentralrechner für massive Datenverarbeitung und hohe Verfügbarkeit",
         "Ein einfacher Heimcomputer",
         "Ein mobiles Endgerät",
         "Ein Spielkonsolenprototyp"),

        ("In welchen Bereichen werden Mainframes häufig eingesetzt?",
         "Banken, Versicherungen, Regierungsbehörden, Industrie, Luftfahrt",
         "Nur in kleinen Büros",
         "In jedem Haushalt",
         "In kleinen Einzelhandelsgeschäften"),

        ("Warum sind Mainframes so wichtig?",
         "Höchste Zuverlässigkeit, Skalierbarkeit, enorme Rechenleistung, Sicherheit, Abwärtskompatibilität",
         "Weil sie günstig und einfach zu bedienen sind",
         "Weil sie klein und kompakt sind",
         "Weil sie ausschließlich für Spiele genutzt werden können"),

        ("Wie hoch ist die Verfügbarkeit von Mainframes?",
         "99.999 % (weniger als 5 Minuten Ausfallzeit pro Jahr)",
         "80 %",
         "50 %",
         "100 %"),

        ("Welche Vorteile bieten Mainframes hinsichtlich Skalierbarkeit?",
         "Können tausende Benutzer gleichzeitig bedienen",
         "Können maximal 10 Benutzer gleichzeitig bedienen",
         "Können nicht skaliert werden",
         "Sind nur für Einzelbenutzer geeignet"),

        ("Wie viele Cores und wie viel RAM können aktuelle Mainframe-Systeme besitzen?",
         "Bis zu 200 Cores und 40 TB RAM",
         "Maximal 4 Cores und 16 GB RAM",
         "Bis zu 8 Cores und 32 GB RAM",
         "Bis zu 16 Cores und 64 GB RAM"),

        ("Welche Vorteile bieten Mainframes in Bezug auf Sicherheit?",
         "Unterstützen verschlüsselte Transaktionen (bis zu 25 Milliarden pro Tag)",
         "Haben keine Sicherheitsfunktionen",
         "Sind nur durch einfache Passwörter gesichert",
         "Nutzen keine Verschlüsselung"),

        ("Was beschreibt die Abwärtskompatibilität von Mainframes?",
         "Software von 1965 (IBM S/360) kann immer noch ausgeführt werden",
         "Nur moderne Software kann ausgeführt werden",
         "Software wird nach 2 Jahren veraltet",
         "Abwärtskompatibilität ist nicht möglich"),

        ("Welche Hauptkomponenten hat ein Mainframe?",
         "Mehrkern-CPUs, RAM, Festplattensysteme, I/O-Prozessoren, Bandroboter",
         "Nur eine CPU und eine Festplatte",
         "Keine spezialisierte Hardware",
         "Nur eine einfache Speicherkarte"),

        ("Welche Vorteile bietet die spezialisierte I/O-Architektur von Mainframes?",
         "Kann riesige Datenmengen verarbeiten",
         "Kann nur kleine Datenmengen verarbeiten",
         "Bietet keine besonderen Vorteile",
         "Ist langsamer als bei normalen Servern"),

        ("Was bedeutet parallele Verarbeitung in Mainframes?",
         "Mehrere Datenströme gleichzeitig verarbeiten",
         "Nur ein Datenstrom gleichzeitig verarbeiten",
         "Keine parallele Verarbeitung möglich",
         "Langsame Datenverarbeitung"),

        ("Wie lange bleiben Mainframes bei Hardwarefehlern online?",
         "Ohne Unterbrechung",
         "Maximal 1 Stunde",
         "Maximal 10 Minuten",
         "Sie werden sofort abgeschaltet"),

        ("Welche I/O-Konzepte sind für Mainframes besonders wichtig?",
         "Parallele Verarbeitung, spezialisierte Hardware für I/O, hochsichere Speicherlösungen",
         "Keine besonderen Konzepte",
         "Nur einfache I/O-Konzepte",
         "Langsame Verarbeitung"),

        ("Welche Entwicklungen sind in der Zukunft der Mainframes zu erwarten?",
         "Linux auf Mainframes, KI, Energieeffizienz",
         "Mainframes werden verschwinden",
         "Nur begrenzte Weiterentwicklungen",
         "Keine weiteren Entwicklungen"),

        ("Warum unterstützen moderne Mainframes z/Linux?",
         "Für flexiblere Nutzung",
         "Um altmodisch zu bleiben",
         "Um ineffizient zu sein",
         "Nur aus Marketinggründen"),

        ("Welche Rolle spielt Künstliche Intelligenz (KI) bei modernen Mainframes?",
         "KI-basierte Datenanalysen laufen immer häufiger auf Mainframes",
         "Keine Rolle",
         "Nur im Zusammenhang mit Spielen",
         "Nur für einfache Berechnungen"),

        ("Was ist ein Beispiel für die Energieeffizienz moderner Mainframes?",
         "Neue Mainframes verbrauchen weniger Strom bei höherer Leistung",
         "Mainframes verbrauchen viel mehr Strom als normale Computer",
         "Mainframes haben keine besonderen Energieeigenschaften",
         "Mainframes sind nur für Hochleistungsanwendungen gedacht"),

        ("Wie viele verschlüsselte Transaktionen pro Tag kann der IBM z15 Mainframe verarbeiten?",
         "1 Milliarde",
         "100.000",
         "1 Million",
         "10 Millionen"),

        ("Warum sind Mainframes für das Finanzsystem wichtig?",
         "Die meisten Banktransaktionen weltweit laufen über Mainframes",
         "Weil sie für Spiele genutzt werden",
         "Weil sie günstig sind",
         "Weil sie tragbar sind"),

        ("Welche Speicherlösungen verwenden Mainframes oft für große Datenmengen?",
         "Magnetbänder oder RAID-Systeme",
         "Nur einfache Festplatten",
         "Nur SSDs",
         "Keine besonderen Speicherlösungen"),
    ]

class Virtualisierung:
    questions = [
        ("Was ist Virtualisierung?",
         "Trennung von physischen und logischen Ressourcen, sodass Betriebssysteme und Anwendungen unabhängig von der zugrundeliegenden Hardware laufen können",
         "Eine Methode zur Beschleunigung der Datenübertragung",
         "Eine Sicherheitsmaßnahme gegen Malware",
         "Ein Netzwerkdienst zur Kommunikation zwischen Computern"),

        ("Welche Vorteile bietet die Virtualisierung?",
         "Effizientere Hardware-Nutzung, erhöhte Ausfallsicherheit, Flexibilität & Skalierbarkeit, bessere Verwaltung von IT-Ressourcen",
         "Geringere Hardware-Nutzung, niedrigere Ausfallsicherheit, eingeschränkte Flexibilität",
         "Erhöhte Kosten, verringerte Performance",
         "Nur geeignet für Heim-PCs"),

        ("Was ist ein Hypervisor?",
         "Eine Software-Schicht, die virtuelle Maschinen verwaltet und ihnen Zugriff auf die Hardware gibt",
         "Ein spezieller Hardware-Chip zur Leistungssteigerung",
         "Ein Netzwerkprotokoll für sichere Kommunikation",
         "Ein Backup-Tool für Datenwiederherstellung"),

        ("Welche Arten von Hypervisoren gibt es?",
         "Typ-1 (Bare-Metal) und Typ-2 (Hosted)",
         "Typ-3 (Cloud) und Typ-4 (Hybrid)",
         "Nur Typ-1 (Bare-Metal)",
         "Nur Typ-2 (Hosted)"),

        ("Was ist ein Typ-1 (Bare-Metal) Hypervisor?",
         "Läuft direkt auf der Hardware, kein Host-OS notwendig",
         "Läuft als Anwendung auf einem bestehenden OS",
         "Ist nur eine theoretische Konzeption",
         "Wird ausschließlich für Grafikprozessoren verwendet"),

        ("Was ist ein Typ-2 (Hosted) Hypervisor?",
         "Läuft als Anwendung auf einem bestehenden OS",
         "Läuft direkt auf der Hardware",
         "Wird nur in Cloud-Umgebungen verwendet",
         "Ist eine veraltete Virtualisierungsmethode"),

        ("Welche Vorteile bietet ein Typ-1 Hypervisor?",
         "Schneller und stabiler, weil er direkt mit der Hardware arbeitet",
         "Einfacher zu installieren und zu verwenden",
         "Flexibler, aber langsamer",
         "Nur geeignet für Desktops"),

        ("Welche Vorteile bietet ein Typ-2 Hypervisor?",
         "Flexibler, aber langsamer, da er auf einem bestehenden OS läuft",
         "Schneller und stabiler, weil er direkt mit der Hardware arbeitet",
         "Nur für Server geeignet",
         "Nur für Virtualisierungsumgebungen geeignet"),

        ("Wie viele Betriebssysteme können auf einer virtuellen Maschine gleichzeitig laufen?",
         "Mehrere Betriebssysteme parallel auf einer Maschine",
         "Nur ein Betriebssystem pro Maschine",
         "Keine Betriebssysteme",
         "Nur zwei Betriebssysteme gleichzeitig"),

        ("Was ist ein Beispiel für einen Typ-1 Hypervisor?",
         "VMware ESXi",
         "VirtualBox",
         "VMware Workstation",
         "Parallels Desktop"),

        ("Was ist ein Beispiel für einen Typ-2 Hypervisor?",
         "VirtualBox",
         "VMware ESXi",
         "Microsoft Hyper-V",
         "Xen"),

        ("Warum ist Virtualisierung ideal für Tests & Softwareentwicklung?",
         "Virtuelle Maschinen können schnell erstellt, kopiert oder migriert werden",
         "Virtuelle Maschinen sind sehr langsam",
         "Virtuelle Maschinen benötigen spezielle Hardware",
         "Virtuelle Maschinen sind schwer zu verwalten"),

        ("Was ist eine virtuelle Maschine (VM)?",
         "Eine simulierte Computerumgebung innerhalb eines anderen Systems",
         "Ein physischer Server mit mehreren Benutzerzugängen",
         "Ein Netzwerkknoten für Datenübertragung",
         "Ein Backup-Tool für Datenwiederherstellung"),

        ("Wie unterstützt Virtualisierung die Flexibilität und Skalierbarkeit?",
         "Virtuelle Maschinen können schnell erstellt, kopiert oder migriert werden",
         "Virtuelle Maschinen sind sehr starr und unflexibel",
         "Virtuelle Maschinen sind nur für kleine Netzwerke geeignet",
         "Virtuelle Maschinen benötigen spezielle Netzwerkprotokolle"),

        ("Welche Hauptkomponente verwaltet die virtuellen Maschinen?",
         "Hypervisor",
         "Kernel",
         "Netzwerkprotokoll",
         "Backup-Tool"),

        ("Welche Vorteile bietet Virtualisierung in Bezug auf Ausfallsicherheit?",
         "Falls ein System abstürzt, bleibt der Host stabil",
         "Wenn ein System abstürzt, stürzt der Host ebenfalls ab",
         "Keine speziellen Vorteile",
         "Erhöhte Anfälligkeit für Fehler"),

        ("Was beschreibt die Trennung von physischen und logischen Ressourcen bei der Virtualisierung?",
         "Betriebssysteme und Anwendungen laufen unabhängig von der zugrundeliegenden Hardware",
         "Betriebssysteme und Anwendungen sind direkt an die Hardware gebunden",
         "Keine Trennung möglich",
         "Nur eine theoretische Konzeption"),

        ("Welche Komponente ermöglicht die Abstraktion von Hardware bei der Virtualisierung?",
         "Hypervisor",
         "Netzwerkprotokoll",
         "Speicherverwaltungsprozess",
         "Grafikkartentreiber"),

        ("Welche Sicherheitsvorteile bietet die Virtualisierung?",
         "Jede VM läuft isoliert, was die Sicherheit erhöht",
         "Alle VMs teilen sich denselben Sicherheitskontext",
         "Keine speziellen Sicherheitsvorteile",
         "Virtuelle Maschinen sind unsicherer als physische Systeme"),

        ("Wie funktioniert die Verwaltung von IT-Ressourcen bei der Virtualisierung?",
         "IT-Umgebungen lassen sich zentral verwalten",
         "IT-Umgebungen sind schwer zu verwalten",
         "IT-Ressourcen sind nicht skalierbar",
         "IT-Umgebungen sind nicht flexibel"),
    ]


class CPUScheduling:
    questions = [
        ("Was ist CPU-Scheduling?",
         "Der Mechanismus, der bestimmt, welcher Prozess zu welcher Zeit die CPU nutzen darf",
         "Eine Methode zur Speicherverwaltung",
         "Ein Sicherheitsprotokoll",
         "Ein Netzwerkdienst zur Datenübertragung"),

        ("Was ist Multitasking?",
         "Mehrere Prozesse laufen scheinbar gleichzeitig durch schnelles Umschalten",
         "Ein Prozess wird auf mehrere CPUs verteilt",
         "Nur ein Prozess kann zur gleichen Zeit laufen",
         "Eine Methode zur Datenkomprimierung"),

        ("Was ist ein Dispatcher?",
         "Schaltet Prozesse um (Dispatcher-Latenz = Zeit für den Wechsel)",
         "Ein Speichermanagement-Tool",
         "Ein Netzwerkprotokoll",
         "Ein Dateiverwaltungsprozess"),

        ("Was beschreibt CPU-Burst?",
         "Zeit, in der ein Prozess ununterbrochen die CPU nutzt",
         "Zeit, die ein Prozess im Speicher verbleibt",
         "Zeit, die ein Prozess auf I/O wartet",
         "Zeit, die ein Prozess zum Laden von Dateien benötigt"),

        ("Was ist der Unterschied zwischen I/O-Bound und CPU-Bound Prozessen?",
         "I/O-Bound Prozesse nutzen mehr Ein-/Ausgabe, CPU-Bound Prozesse brauchen hauptsächlich Rechenleistung",
         "I/O-Bound Prozesse benötigen mehr Rechenleistung",
         "CPU-Bound Prozesse nutzen mehr Ein-/Ausgabe",
         "Es gibt keinen Unterschied"),

        ("Was ist der Scheduler?",
         "Der Mechanismus, der entscheidet, wann und welcher Prozess läuft",
         "Eine Methode zur Speicherverwaltung",
         "Ein Sicherheitsprotokoll",
         "Ein Netzwerkdienst zur Datenübertragung"),

        ("Was bedeutet CPU-Auslastung als Scheduling-Kriterium?",
         "Die CPU sollte möglichst nie untätig sein",
         "Die CPU sollte möglichst oft untätig sein",
         "Die CPU sollte eine bestimmte Temperatur nicht überschreiten",
         "Die CPU sollte immer im Leerlauf sein"),

        ("Was beschreibt Durchsatz als Scheduling-Kriterium?",
         "Anzahl der Prozesse, die pro Zeiteinheit abgeschlossen werden",
         "Zeit von der Ankunft eines Prozesses bis zur Beendigung",
         "Zeit, die ein Prozess im Speicher verbleibt",
         "Zeit, die ein Prozess zum Laden von Dateien benötigt"),

        ("Was beschreibt Turnaround-Zeit als Scheduling-Kriterium?",
         "Zeit von der Ankunft eines Prozesses bis zur Beendigung",
         "Anzahl der Prozesse, die pro Zeiteinheit abgeschlossen werden",
         "Zeit, die ein Prozess im Speicher verbleibt",
         "Zeit, die ein Prozess zum Laden von Dateien benötigt"),

        ("Was beschreibt Wartezeit als Scheduling-Kriterium?",
         "Zeit, die ein Prozess in der Ready-Queue verbringt",
         "Zeit von der Ankunft eines Prozesses bis zur Beendigung",
         "Zeit, die ein Prozess im Speicher verbleibt",
         "Zeit, die ein Prozess zum Laden von Dateien benötigt"),

        ("Was beschreibt Antwortzeit als Scheduling-Kriterium?",
         "Zeit, bis ein Prozess zum ersten Mal CPU-Zeit erhält",
         "Zeit von der Ankunft eines Prozesses bis zur Beendigung",
         "Zeit, die ein Prozess im Speicher verbleibt",
         "Zeit, die ein Prozess zum Laden von Dateien benötigt"),

        ("Was bedeutet Fairness als Scheduling-Kriterium?",
         "Kein Prozess darf unfair benachteiligt werden",
         "Die CPU sollte möglichst oft untätig sein",
         "Die CPU sollte eine bestimmte Temperatur nicht überschreiten",
         "Die CPU sollte immer im Leerlauf sein"),

        ("Was ist First Come, First Served (FCFS) Scheduling?",
         "Prozesse werden in der Reihenfolge ausgeführt, in der sie ankommen",
         "Prozesse mit kürzester Rechenzeit werden bevorzugt",
         "Jeder Prozess erhält ein festes Zeitquantum",
         "Jeder Prozess hat eine Priorität"),

        ("Was ist das Problem beim FCFS Scheduling?",
         "Konvoi-Effekt -> Kurze Prozesse müssen lange auf lange Prozesse warten",
         "Zu kurze Zeitquantums -> hoher Overhead durch ständige Kontextwechsel",
         "Kann zu Starvation führen",
         "Keine Probleme"),

        ("Was ist Shortest Job First (SJF) Scheduling?",
         "Prozesse mit kürzester Rechenzeit werden bevorzugt",
         "Prozesse werden in der Reihenfolge ausgeführt, in der sie ankommen",
         "Jeder Prozess erhält ein festes Zeitquantum",
         "Jeder Prozess hat eine Priorität"),

        ("Was ist das Problem beim SJF Scheduling?",
         "Kann zu Starvation führen (lange Prozesse warten ewig)",
         "Konvoi-Effekt -> Kurze Prozesse müssen lange auf lange Prozesse warten",
         "Zu kurze Zeitquantums -> hoher Overhead durch ständige Kontextwechsel",
         "Keine Probleme"),

        ("Was ist Round Robin (RR) Scheduling?",
         "Jeder Prozess erhält ein festes Zeitquantum (z. B. 10 ms)",
         "Prozesse mit kürzester Rechenzeit werden bevorzugt",
         "Prozesse werden in der Reihenfolge ausgeführt, in der sie ankommen",
         "Jeder Prozess hat eine Priorität"),

        ("Was ist das Problem beim RR Scheduling?",
         "Zu kurze Zeitquantums -> hoher Overhead durch ständige Kontextwechsel",
         "Konvoi-Effekt -> Kurze Prozesse müssen lange auf lange Prozesse warten",
         "Kann zu Starvation führen",
         "Keine Probleme"),

        ("Was ist Priority Scheduling?",
         "Jeder Prozess hat eine Priorität (niedrigere Zahl = höhere Priorität)",
         "Prozesse mit kürzester Rechenzeit werden bevorzugt",
         "Prozesse werden in der Reihenfolge ausgeführt, in der sie ankommen",
         "Jeder Prozess erhält ein festes Zeitquantum"),

        ("Was ist das Problem beim Priority Scheduling?",
         "Starvation -> Niedrigpriorisierte Prozesse können blockiert werden",
         "Zu kurze Zeitquantums -> hoher Overhead durch ständige Kontextwechsel",
         "Konvoi-Effekt -> Kurze Prozesse müssen lange auf lange Prozesse warten",
         "Keine Probleme"),
    ]


class ProzesseInBetriebssystemen:
    questions = [
        ("Was ist ein Prozess?",
         "Ein laufendes Programm, das durch das Betriebssystem verwaltet wird",
         "Eine Datei auf der Festplatte",
         "Ein Netzwerkdienst",
         "Ein Hardware-Komponent"),

        ("Was ist der Unterschied zwischen einem Programm und einem Prozess?",
         "Ein Programm ist passiv (Datei auf Festplatte), ein Prozess ist aktiv (läuft in der CPU/RAM)",
         "Es gibt keinen Unterschied",
         "Ein Programm ist aktiv, ein Prozess ist passiv",
         "Ein Programm läuft nur im Speicher"),

        ("In welchen Zuständen kann sich ein Prozess befinden?",
         "New, Running, Ready, Blocked (Wait), Terminated",
         "Start, Stop, Pause, Resume",
         "Aktiv, Inaktiv, Schlafend",
         "Eingabe, Verarbeitung, Ausgabe"),

        ("Was ist der Prozesskontrollblock (PCB)?",
         "Eine Datenstruktur, die alle Informationen über einen Prozess enthält",
         "Ein Speicherverwaltungsprozess",
         "Ein Netzwerkdienst",
         "Eine Dateiverwaltungsfunktion"),

        ("Welche Informationen enthält der Prozesskontrollblock (PCB)?",
         "PID, Prozesszustand, Register & Befehlszähler, Speicherverwaltung, Dateideskriptoren",
         "Nur PID und Speicherverwaltung",
         "Nur Prozesszustand und Register",
         "Nur Dateideskriptoren und Befehlszähler"),

        ("Was ist der Unterschied zwischen Nebenläufigkeit und Parallelität?",
         "Nebenläufigkeit: Prozesse laufen scheinbar gleichzeitig, Parallelität: Prozesse laufen wirklich gleichzeitig auf mehreren CPU-Kernen",
         "Es gibt keinen Unterschied",
         "Nebenläufigkeit: Prozesse laufen nacheinander, Parallelität: Prozesse laufen gleichzeitig auf einem Kern",
         "Nebenläufigkeit: Prozesse laufen auf mehreren Kernen, Parallelität: Prozesse laufen auf einem Kern"),

        ("Was ist ein Kontextwechsel (Context Switch)?",
         "Beim Wechsel zwischen Prozessen muss das OS alle Register, den Stack & den Programmcounter speichern und den neuen Prozess laden",
         "Ein Wechsel der Netzwerkschnittstelle",
         "Ein Speicherverwaltungsprozess",
         "Ein Wechsel der Benutzerschnittstelle"),

        ("Was ist ein Elternprozess?",
         "Ein Prozess, der andere Prozesse erzeugt",
         "Ein Prozess, der beendet wurde",
         "Ein Prozess, der im Hintergrund läuft",
         "Ein Prozess, der keine Kindprozesse hat"),

        ("Was ist ein Kindprozess?",
         "Ein Prozess, der von einem anderen Prozess erzeugt wurde",
         "Ein Prozess, der im Hintergrund läuft",
         "Ein Prozess, der keine Elternprozesse hat",
         "Ein Prozess, der beendet wurde"),

        ("Was ist Prozesskommunikation (IPC)?",
         "Prozesse können miteinander kommunizieren, z.B. durch Signale, Nachrichten oder Shared Memory",
         "Ein Netzwerkprotokoll für Datenübertragung",
         "Ein Sicherheitsmechanismus",
         "Eine Speichermanagementtechnik"),

        ("Warum ist Prozesssynchronisation wichtig?",
         "Um Inkonsistenzen und Fehler bei gleichzeitigem Zugriff auf gemeinsame Ressourcen zu vermeiden",
         "Um die CPU-Auslastung zu erhöhen",
         "Um Netzwerkanforderungen zu optimieren",
         "Um Speicher effizienter zu nutzen"),

        ("Was ist eine Race Condition?",
         "Zwei Prozesse greifen gleichzeitig auf eine Variable zu, wodurch unvorhersehbare Ergebnisse entstehen",
         "Ein Speicherverwaltungsproblem",
         "Ein Netzwerkfehler",
         "Ein Hardwaredefekt"),

        ("Was ist ein kritischer Abschnitt?",
         "Ein Codebereich, in dem gemeinsam genutzte Daten verändert werden",
         "Ein Bereich im Betriebssystemkern",
         "Ein Speichersegment",
         "Ein Abschnitt im Dateisystem"),

        ("Was ist Mutual Exclusion?",
         "Nur ein Prozess darf zur gleichen Zeit im kritischen Abschnitt sein",
         "Mehrere Prozesse dürfen gleichzeitig im kritischen Abschnitt sein",
         "Prozesse dürfen nie im kritischen Abschnitt sein",
         "Nur Hintergrundprozesse dürfen im kritischen Abschnitt sein"),

        ("Was ist ein Semaphor?",
         "Eine spezielle ganzzahlige Variable, die als Synchronisationsmechanismus dient",
         "Ein Netzwerkprotokoll",
         "Ein Speichermanagementprozess",
         "Ein Hardwaretreiber"),

        ("Was sind die Haupttypen von Semaphoren?",
         "Binärer Semaphor und Zählender Semaphor",
         "Einfacher Semaphor und komplexer Semaphor",
         "Interner Semaphor und externer Semaphor",
         "Statischer Semaphor und dynamischer Semaphor"),

        ("Welche Operationen werden bei Semaphoren verwendet?",
         "wait(S) und signal(S)",
         "start(S) und stop(S)",
         "enable(S) und disable(S)",
         "open(S) und close(S)"),

        ("Was ist ein Deadlock?",
         "Eine Situation, in der zwei oder mehr Prozesse sich gegenseitig blockieren und keines weiterkommt",
         "Ein Netzwerkproblem",
         "Ein Speicherverwaltungsfehler",
         "Ein Hardwareausfall"),

        ("Wie kann man Deadlocks vermeiden?",
         "Durch Ressourcenallokationsstrategien, Deadlock-Vermeidung und -Erkennungsmethoden",
         "Durch Erhöhung der CPU-Geschwindigkeit",
         "Durch Nutzung von mehr Speicher",
         "Durch Abschaltung des Systems"),

        ("Was ist der Unterschied zwischen Deadlock-Vermeidung und Deadlock-Erkennung?",
         "Vermeidung: Strategien, um Deadlocks zu verhindern; Erkennung: Methoden, um Deadlocks zu erkennen und zu beheben",
         "Es gibt keinen Unterschied",
         "Vermeidung: Deadlocks ignorieren; Erkennung: Deadlocks nicht erkennen",
         "Vermeidung: Deadlocks provozieren; Erkennung: Deadlocks akzeptieren"),
    ]


class Prozesssynchronisation:
    questions = [
        ("Warum ist Prozesssynchronisation notwendig?",
         "Um Inkonsistenzen und Fehler bei gleichzeitigem Zugriff auf gemeinsame Ressourcen zu vermeiden",
         "Um die CPU-Auslastung zu erhöhen",
         "Um Netzwerkanforderungen zu optimieren",
         "Um Speicher effizienter zu nutzen"),

        ("Was ist eine Race Condition?",
         "Zwei Prozesse greifen gleichzeitig auf eine Variable zu, wodurch unvorhersehbare Ergebnisse entstehen",
         "Ein Speicherverwaltungsproblem",
         "Ein Netzwerkfehler",
         "Ein Hardwaredefekt"),

        ("Was ist ein kritischer Abschnitt?",
         "Ein Codebereich, in dem gemeinsam genutzte Daten verändert werden",
         "Ein Bereich im Betriebssystemkern",
         "Ein Speichersegment",
         "Ein Abschnitt im Dateisystem"),

        ("Was ist Mutual Exclusion?",
         "Nur ein Prozess darf zur gleichen Zeit im kritischen Abschnitt sein",
         "Mehrere Prozesse dürfen gleichzeitig im kritischen Abschnitt sein",
         "Prozesse dürfen nie im kritischen Abschnitt sein",
         "Nur Hintergrundprozesse dürfen im kritischen Abschnitt sein"),

        ("Was ist ein Semaphor?",
         "Eine spezielle ganzzahlige Variable, die als Synchronisationsmechanismus dient",
         "Ein Netzwerkprotokoll",
         "Ein Speichermanagementprozess",
         "Ein Hardwaretreiber"),

        ("Welche Haupttypen von Semaphoren gibt es?",
         "Binärer Semaphor und Zählender Semaphor",
         "Einfacher Semaphor und Komplexer Semaphor",
         "Interner Semaphor und Externer Semaphor",
         "Statischer Semaphor und Dynamischer Semaphor"),

        ("Welche Operationen werden bei Semaphoren verwendet?",
         "wait(S) und signal(S)",
         "start(S) und stop(S)",
         "enable(S) und disable(S)",
         "open(S) und close(S)"),

        ("Was ist ein Deadlock?",
         "Eine Situation, in der zwei oder mehr Prozesse sich gegenseitig blockieren und keines weiterkommt",
         "Ein Netzwerkproblem",
         "Ein Speicherverwaltungsfehler",
         "Ein Hardwareausfall"),

        ("Wie kann man Deadlocks vermeiden?",
         "Durch Ressourcenallokationsstrategien, Deadlock-Vermeidung und -Erkennungsmethoden",
         "Durch Erhöhung der CPU-Geschwindigkeit",
         "Durch Nutzung von mehr Speicher",
         "Durch Abschaltung des Systems"),

        ("Was ist der Unterschied zwischen Deadlock-Vermeidung und Deadlock-Erkennung?",
         "Vermeidung: Strategien, um Deadlocks zu verhindern; Erkennung: Methoden, um Deadlocks zu erkennen und zu beheben",
         "Es gibt keinen Unterschied",
         "Vermeidung: Deadlocks ignorieren; Erkennung: Deadlocks nicht erkennen",
         "Vermeidung: Deadlocks provozieren; Erkennung: Deadlocks akzeptieren"),

        ("Was ist ein Monitor in der Prozesssynchronisation?",
         "Ein höheres Abstraktionsniveau für die Synchronisation, bietet automatische Sperr- und Entsperrfunktion",
         "Ein Netzwerküberwachungs-Tool",
         "Ein Hardwarediagnose-Tool",
         "Ein Speichermanagementprozess"),

        ("Was beschreibt das 'Lost Update Problem'?",
         "Ein Prozess überschreibt eine Änderung eines anderen Prozesses",
         "Ein Netzwerkproblem",
         "Ein Speicherverwaltungsfehler",
         "Ein Hardwaredefekt"),

        ("Was ist das 'Dirty Read Problem'?",
         "Ein Prozess liest eine noch nicht abgeschlossene Änderung eines anderen Prozesses",
         "Ein Netzwerkproblem",
         "Ein Speicherverwaltungsfehler",
         "Ein Hardwaredefekt"),

        ("Was ist das Bounded-Buffer-Problem?",
         "Ein Synchronisationsproblem, bei dem ein endlicher Puffer genutzt wird, um Daten zwischen Produzenten und Konsumenten auszutauschen",
         "Ein Netzwerkproblem",
         "Ein Speicherverwaltungsfehler",
         "Ein Hardwaredefekt"),

        ("Welche Synchronisationsmechanismen gibt es neben Semaphoren?",
         "Mutex, Monitor, Sperrvariable, Peterson's Algorithmus, Test-and-Set (TSL)",
         "Nur Mutex und Monitor",
         "Nur Sperrvariable und Test-and-Set (TSL)",
         "Nur Peterson's Algorithmus und TSL"),

        ("Was ist eine Mutex?",
         "Eine spezielle Art von Semaphor, die immer binär ist und für gegenseitigen Ausschluss verwendet wird",
         "Ein Netzwerkprotokoll",
         "Ein Speichermanagementprozess",
         "Ein Hardwaretreiber"),

        ("Was ist Peterson's Algorithmus?",
         "Ein Algorithmus für gegenseitigen Ausschluss, der nur mit zwei Prozessen funktioniert",
         "Ein Netzwerkprotokoll",
         "Ein Speicherverwaltungsalgorithmus",
         "Ein Dateisystemalgorithmus"),

        ("Was ist ein Beispiel für eine Deadlock-Erkennungsmethode?",
         "Ressourcenzuteilungsgraphen",
         "Rundlaufzeiten",
         "Durchsatzberechnung",
         "CPU-Auslastungsprotokoll"),

        ("Was ist die Philosophenproblem?",
         "Ein klassisches Synchronisationsproblem, bei dem Philosophen zwischen Denken und Essen wechseln und Gabeln teilen müssen",
         "Ein Speicherverwaltungsproblem",
         "Ein Netzwerkproblem",
         "Ein Hardwaredefekt"),

        ("Wie kann das Philosophenproblem gelöst werden?",
         "Durch die Nutzung von Semaphoren oder Monitore zur Steuerung des Zugriffs auf Ressourcen",
         "Durch Erhöhung der CPU-Geschwindigkeit",
         "Durch Nutzung von mehr Speicher",
         "Durch Abschaltung des Systems"),
    ]


class Speicherverwaltung:
    questions = [
        ("Was ist Speicherverwaltung?",
         "Die effiziente Zuteilung und Verwaltung des Arbeitsspeichers durch das Betriebssystem",
         "Ein Netzwerkdienst zur Datenübertragung",
         "Ein Sicherheitsprotokoll",
         "Ein Prozess zur Dateiverwaltung"),

        ("Was sind die Hauptaufgaben der Speicherverwaltung?",
         "Zuweisung von Speicher an Programme, Schutz des Speichers, Verwaltung des virtuellen Speichers",
         "Nur Zuweisung von Speicher an Programme",
         "Nur Schutz des Speichers",
         "Nur Verwaltung des virtuellen Speichers"),

        ("Was ist der Unterschied zwischen Monoprogramming und Multiprogramming?",
         "Monoprogramming lässt nur ein Programm im Speicher laufen, während Multiprogramming mehrere Programme gleichzeitig laufen lässt",
         "Monoprogramming läuft schneller",
         "Multiprogramming lässt nur ein Programm im Speicher laufen",
         "Es gibt keinen Unterschied"),

        ("Was ist Paging?",
         "Eine Technik zur Verwaltung des Speichers durch Aufteilen in gleich große Seiten",
         "Ein Netzwerkprotokoll",
         "Ein Sicherheitsprotokoll",
         "Eine Methode zur Prozessverwaltung"),

        ("Was ist eine Seitentabelle (Page Table)?",
         "Eine Datenstruktur, die die Zuordnung von virtuellen Seiten zu physischen Frames verwaltet",
         "Eine Tabelle zur Prozessverwaltung",
         "Ein Netzwerkdiagramm",
         "Eine Liste der geöffneten Dateien"),

        ("Was ist ein Seitenfehler (Page Fault)?",
         "Wenn eine benötigte Seite nicht im Speicher ist und von der Festplatte geladen werden muss",
         "Ein Fehler im Netzwerk",
         "Ein Fehler im Dateisystem",
         "Ein Hardwaredefekt"),

        ("Was ist der Vorteil von Paging?",
         "Kein externer Speicherverlust, erlaubt virtuellen Speicher",
         "Langsame Speicherzugriffe",
         "Erhöhte Fragmentierung",
         "Verschlechterte Speichernutzung"),

        ("Was ist ein Nachteil von Paging?",
         "Seitentabellen können sehr groß werden, Seitenfehler können langsam sein",
         "Erhöhte Fragmentierung",
         "Langsame Speicherzugriffe",
         "Verschlechterte Speichernutzung"),

        ("Was ist die Speicherhierarchie?",
         "Die Anordnung von Speicherarten nach Geschwindigkeit und Kosten",
         "Eine Netzwerktopologie",
         "Eine Liste von Dateitypen",
         "Eine Methode zur Prozessverwaltung"),

        ("Was ist ein Beispiel für Primärspeicher?",
         "RAM, Register",
         "Festplatte",
         "Magnetband",
         "Cloud-Speicher"),

        ("Was ist ein Beispiel für Sekundärspeicher?",
         "Festplatte, SSD",
         "RAM",
         "Register",
         "CPU-Cache"),

        ("Was ist ein Beispiel für Tertiärspeicher?",
         "Magnetband, Backup-Systeme",
         "RAM",
         "Festplatte",
         "SSD"),

        ("Was ist die Memory Management Unit (MMU)?",
         "Ein Hardwarebaustein, der die Adressumwandlung von virtuellen zu physischen Adressen durchführt",
         "Ein Netzwerkcontroller",
         "Ein Sicherheitschip",
         "Ein Prozessor für Grafikverarbeitung"),

        ("Was ist Swapping?",
         "Das Verschieben von ganzen Prozessen zwischen RAM und Festplatte",
         "Das Wechseln von Netzwerkschnittstellen",
         "Das Übertragen von Daten zwischen Prozessen",
         "Das Synchronisieren von Dateien"),

        ("Was ist Demand Paging?",
         "Nur benötigte Seiten werden in den RAM geladen",
         "Alle Seiten werden im Voraus geladen",
         "Ein Netzwerkprotokoll für Datenübertragung",
         "Eine Sicherheitsmaßnahme für Datenintegrität"),

        ("Was ist Pre-Paging?",
         "Seiten werden im Voraus geladen, um Verzögerungen zu vermeiden",
         "Nur benötigte Seiten werden in den RAM geladen",
         "Ein Netzwerkprotokoll",
         "Ein Sicherheitsprotokoll"),

        ("Was ist eine Ersetzungsstrategie (Page Replacement)?",
         "Ein Algorithmus, der entscheidet, welche Seite bei Speicherknappheit ersetzt wird",
         "Ein Verfahren zur Prozessverwaltung",
         "Ein Netzwerkprotokoll",
         "Ein Sicherheitsmechanismus"),

        ("Was ist FIFO (First In, First Out) bei der Ersetzung?",
         "Die älteste Seite wird ersetzt",
         "Die jüngste Seite wird ersetzt",
         "Die am meisten genutzte Seite wird ersetzt",
         "Die am wenigsten genutzte Seite wird ersetzt"),

        ("Was ist LRU (Least Recently Used) bei der Ersetzung?",
         "Die am längsten ungenutzte Seite wird ersetzt",
         "Die am kürzesten genutzte Seite wird ersetzt",
         "Die älteste Seite wird ersetzt",
         "Die jüngste Seite wird ersetzt"),

        ("Was beschreibt Belady's Anomalie?",
         "Paradoxerweise mehr Seitenfehler bei mehr verfügbarem Speicher",
         "Weniger Seitenfehler bei weniger verfügbarem Speicher",
         "Eine Anomalie im Netzwerkprotokoll",
         "Ein Fehler im Dateisystem"),
    ]


class FestplattenRAID:
    questions = [
        ("Was ist eine Festplatte (HDD)?",
         "Eine magnetische Speichertechnologie mit rotierenden Scheiben",
         "Ein Flash-Speichergerät",
         "Ein optisches Speichermedium",
         "Ein Cloud-Speichersystem"),

        ("Was sind die Vorteile von HDDs?",
         "Große Speicherkapazität zu niedrigen Kosten",
         "Extrem schnelle Zugriffszeiten",
         "Geringer Energieverbrauch",
         "Mechanische Robustheit"),

        ("Was sind die Nachteile von HDDs?",
         "Langsame Zugriffszeit durch mechanische Bewegung",
         "Hohe Speicherkapazität",
         "Geringe Kosten",
         "Kein mechanischer Verschleiß"),

        ("Was ist eine SSD (Solid State Drive)?",
         "Ein Flash-Speichergerät ohne bewegliche Teile",
         "Eine magnetische Speichertechnologie",
         "Ein optisches Speichermedium",
         "Ein Bandlaufwerk"),

        ("Welche Vorteile bieten SSDs?",
         "Extrem schnelle Zugriffszeiten, geringer Energieverbrauch, mechanische Robustheit",
         "Hohe Speicherkapazität",
         "Niedrige Kosten",
         "Langsame Zugriffszeiten"),

        ("Was sind die Nachteile von SSDs?",
         "Höherer Preis pro GB als HDDs, begrenzte Schreib-/Löschzyklen",
         "Hoher Energieverbrauch",
         "Mechanische Defekte",
         "Lange Zugriffszeiten"),

        ("Was ist RAID (Redundant Array of Independent Disks)?",
         "Eine Methode zur Kombination mehrerer Festplatten zur Datenredundanz oder Leistungssteigerung",
         "Ein einzelnes Festplattensystem",
         "Ein optisches Speichermedium",
         "Ein Netzwerkprotokoll"),

        ("Warum wird RAID eingesetzt?",
         "Schutz vor Festplattenausfällen, Performance-Steigerung, Optimierung von Speicherplatz",
         "Erhöhung der Zugriffszeit",
         "Reduzierung der Speicherkapazität",
         "Verschlechterung der Datenintegrität"),

        ("Was ist RAID 0 (Striping)?",
         "Daten werden in Blöcke aufgeteilt und parallel auf mehrere Festplatten geschrieben",
         "Daten werden 1:1 auf zwei Festplatten gespiegelt",
         "Daten werden verteilt gespeichert mit Paritätsinformationen",
         "Daten werden komprimiert gespeichert"),

        ("Was ist der Hauptvorteil von RAID 0?",
         "Sehr hohe Lese-/Schreibgeschwindigkeit",
         "Volle Datensicherheit",
         "Geringer Energieverbrauch",
         "Niedrige Kosten"),

        ("Was ist der Hauptnachteil von RAID 0?",
         "Keine Redundanz, bei Ausfall einer Platte sind alle Daten verloren",
         "Geringe Lese-/Schreibgeschwindigkeit",
         "Hoher Energieverbrauch",
         "Langsame Zugriffszeiten"),

        ("Was ist RAID 1 (Mirroring)?",
         "Daten werden 1:1 auf zwei Festplatten gespiegelt",
         "Daten werden in Blöcke aufgeteilt und parallel auf mehrere Festplatten geschrieben",
         "Daten werden verteilt gespeichert mit Paritätsinformationen",
         "Daten werden komprimiert gespeichert"),

        ("Was ist der Hauptvorteil von RAID 1?",
         "Volle Datensicherheit, eine Festplatte kann ausfallen",
         "Sehr hohe Lese-/Schreibgeschwindigkeit",
         "Geringer Energieverbrauch",
         "Niedrige Kosten"),

        ("Was ist der Hauptnachteil von RAID 1?",
         "Kapazität halbiert sich, da alle Daten doppelt gespeichert werden",
         "Langsame Zugriffszeiten",
         "Hoher Energieverbrauch",
         "Niedrige Speicherkapazität"),

        ("Was ist RAID 5 (Striping mit Parität)?",
         "Daten werden verteilt gespeichert, Paritätsinformationen ermöglichen Wiederherstellung bei Ausfall",
         "Daten werden in Blöcke aufgeteilt und parallel auf mehrere Festplatten geschrieben",
         "Daten werden 1:1 auf zwei Festplatten gespiegelt",
         "Daten werden komprimiert gespeichert"),

        ("Was sind die Vorteile von RAID 5?",
         "Hohe Speichereffizienz, gute Performance beim Lesen",
         "Sehr hohe Lese-/Schreibgeschwindigkeit",
         "Volle Datensicherheit",
         "Niedrige Kosten"),

        ("Was ist der Nachteil von RAID 5?",
         "Schreibzugriffe sind langsamer wegen Paritätsberechnungen",
         "Keine Redundanz",
         "Hoher Energieverbrauch",
         "Langsame Zugriffszeiten"),

        ("Was ist RAID 6 (Doppelte Parität)?",
         "Funktioniert wie RAID 5, aber mit zwei Paritätsblöcken",
         "Daten werden in Blöcke aufgeteilt und parallel auf mehrere Festplatten geschrieben",
         "Daten werden 1:1 auf zwei Festplatten gespiegelt",
         "Daten werden komprimiert gespeichert"),

        ("Was ist der Hauptvorteil von RAID 6?",
         "Extrem hohe Datensicherheit, zwei Festplatten können ausfallen",
         "Sehr hohe Lese-/Schreibgeschwindigkeit",
         "Geringer Energieverbrauch",
         "Niedrige Kosten"),

        ("Was ist der Hauptnachteil von RAID 6?",
         "Noch höhere Schreibverzögerung",
         "Keine Redundanz",
         "Hoher Energieverbrauch",
         "Langsame Zugriffszeiten"),

        ("Was ist RAID 10 (RAID 1 + RAID 0)?",
         "Kombiniert Striping (RAID 0) mit Mirroring (RAID 1)",
         "Daten werden verteilt gespeichert mit Paritätsinformationen",
         "Daten werden in Blöcke aufgeteilt und parallel auf mehrere Festplatten geschrieben",
         "Daten werden komprimiert gespeichert"),

        ("Was sind die Vorteile von RAID 10?",
         "Sehr schnell und sehr ausfallsicher",
         "Geringer Energieverbrauch",
         "Niedrige Kosten",
         "Langsame Zugriffszeiten"),

        ("Was ist der Nachteil von RAID 10?",
         "Benötigt mindestens 4 Festplatten, teuer",
         "Keine Redundanz",
         "Hoher Energieverbrauch",
         "Langsame Zugriffszeiten"),
    ]



class Quiz:
    # Die verfügbaren Kategorien
    categories = [
        ("Grundbegriffe", GrundbegriffeBetriebssystem),
        ("Aufbau Betriebssysteme", AufbauBetriebssysteme),
        ("Shell", UnixShell),
        ("Mainframe", GrossrechnerMainframes),
        ("Virtualisierung", Virtualisierung),
        ("CPU-Scheduling", CPUScheduling),
        ("Prozesse", ProzesseInBetriebssystemen),
        ("Prozesssynchronisation", Prozesssynchronisation),
        ("Speicherverwaltung", Speicherverwaltung),
        ("Festplatten & RAID", FestplattenRAID),
    ]

    def __init__(self):
        self.score = 0
        self.total_questions = 50  # Hier auf 50 stellen
        self.selected_categories = []  # Liste der vom Benutzer ausgewählten Kategorien

    def show_categories(self):
        print("Verfügbare Kategorien:")
        for idx, (name, _) in enumerate(self.categories, 1):
            print(f"{idx}. {name}")

    def select_categories(self):
        self.show_categories()

        # Benutzereingabe für Kategorien
        selected = input(
            "Wählen Sie die Kategorien, aus denen Fragen kommen sollen (z.B. 1, 3, 5 für mehrere Kategorien): ")

        try:
            selected_indexes = [int(x.strip()) - 1 for x in selected.split(",") if x.strip().isdigit()]

            if not selected_indexes:
                raise ValueError

            # Die ausgewählten Kategorien hinzufügen
            self.selected_categories = [self.categories[i][1] for i in selected_indexes]

        except ValueError:
            print("Keine gültigen Kategorien ausgewählt. Standardkategorien werden verwendet.")
            self.selected_categories = [category[1] for category in self.categories]  # Alle Kategorien verwenden

    def start(self):
        print("Willkommen zum IT-Quiz!")

        # Den Benutzer nach den Kategorien fragen
        self.select_categories()

        # Pool aller Fragen aus den ausgewählten Kategorien zusammenstellen
        questions_pool = []
        for category in self.selected_categories:
            questions_pool.extend(category.questions)

        # Wenn weniger als 50 Fragen im Pool sind, wird der Pool auf die vorhandene Anzahl begrenzt
        num_questions = min(self.total_questions, len(questions_pool))

        # 50 zufällige Fragen aus dem Pool auswählen
        selected_questions = random.sample(questions_pool, num_questions)

        # Die ausgewählten Fragen durchgehen
        for i in range(num_questions):
            q, correct, *wrong = selected_questions[i]
            answers = [correct] + wrong
            random.shuffle(answers)

            print(f"\nFrage {i + 1}: {q}")
            for j, answer in enumerate(answers, 1):
                print(f"{j}. {answer}")

            # Schleife bis eine gültige Eingabe erfolgt
            while True:
                try:
                    choice = int(input("Ihre Wahl (1-4): "))

                    # Sicherstellen, dass die Eingabe zwischen 1 und 4 liegt
                    if 1 <= choice <= 4:
                        if answers[choice - 1] == correct:
                            print("Richtig!")
                            self.score += 1
                        else:
                            print(f"Falsch! Die richtige Antwort war: {correct}")
                        break  # Bei einer gültigen Antwort aus der Schleife heraus
                    else:
                        print("Ungültige Eingabe. Bitte geben Sie eine Zahl zwischen 1 und 4 ein.")
                except (ValueError, IndexError):
                    print("Ungültige Eingabe. Bitte geben Sie eine Zahl zwischen 1 und 4 ein.")

        self.calculate_grade()

    def calculate_grade(self):
        percentage = (self.score / self.total_questions) * 100
        if percentage >= 90:
            grade = "1.0"
        elif percentage >= 80:
            grade = "2.0"
        elif percentage >= 70:
            grade = "3.0"
        elif percentage >= 60:
            grade = "4.0"
        else:
            grade = "5.0"

        print(f"\nQuiz beendet! Sie haben {self.score}/{self.total_questions} Fragen richtig beantwortet.")
        print(f"Ihre Note: {grade}")


# Quiz starten
if __name__ == "__main__":
    quiz = Quiz()
    quiz.start()
