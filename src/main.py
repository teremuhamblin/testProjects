import os
import sys
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from process_runner import ProcessRunner

# Déterminer la racine du projet
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BIN_DIR = os.path.join(BASE_DIR, "bin")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("testProjects - Lanceur d'outils")
        self.geometry("750x550")
        self.minsize(600, 400)

        # Icône
        icon_path = os.path.join(ASSETS_DIR, "icon.ico")
        if os.path.exists(icon_path):
            try:
                self.iconbitmap(icon_path)
            except Exception:
                pass

        self.runner = ProcessRunner(
            on_output=self.append_log,
            on_finished=self.on_process_finished
        )

        self._build_ui()
        self.refresh_tools()

    def _build_ui(self):
        # Cadre supérieur : Sélection d'outil et arguments
        top_frame = ttk.LabelFrame(self, text=" Configuration de l'exécution ", padding=10)
        top_frame.pack(fill="x", padx=10, pady=5)

        ttk.Label(top_frame, text="Outil (bin/) :").grid(row=0, column=0, sticky="w", pady=5)
        self.tool_combo = ttk.Combobox(top_frame, state="readonly", width=30)
        self.tool_combo.grid(row=0, column=1, sticky="w", padx=5, pady=5)

        refresh_btn = ttk.Button(top_frame, text="↻", width=3, command=self.refresh_tools)
        refresh_btn.grid(row=0, column=2, padx=2)

        ttk.Label(top_frame, text="Arguments :").grid(row=1, column=0, sticky="w", pady=5)
        self.args_entry = ttk.Entry(top_frame)
        self.args_entry.grid(row=1, column=1, columnspan=2, sticky="ew", padx=5, pady=5)

        # Boutons d'action
        btn_frame = ttk.Frame(top_frame)
        btn_frame.grid(row=2, column=0, columnspan=3, pady=10)

        self.run_btn = ttk.Button(btn_frame, text="Lancer", command=self.start_process)
        self.run_btn.pack(side="left", padx=5)

        self.stop_btn = ttk.Button(btn_frame, text="Arrêter", command=self.stop_process, state="disabled")
        self.stop_btn.pack(side="left", padx=5)

        top_frame.columnconfigure(1, weight=1)

        # Cadre inférieur : Console de sortie
        log_frame = ttk.LabelFrame(self, text=" Sortie console ", padding=10)
        log_frame.pack(fill="both", expand=True, padx=10, pady=5)

        self.log_area = scrolledtext.ScrolledText(log_frame, bg="#1e1e1e", fg="#dcdcdc", insertbackground="white", wrap="word")
        self.log_area.pack(fill="both", expand=True)

    def refresh_tools(self):
        """Scanne le dossier bin pour trouver les exécutables/scripts."""
        if not os.path.exists(BIN_DIR):
            os.makedirs(BIN_DIR)

        tools = [f for f in os.listdir(BIN_DIR) if not f.startswith(".") and os.path.isfile(os.path.join(BIN_DIR, f))]
        self.tool_combo["values"] = tools
        if tools:
            self.tool_combo.current(0)
        else:
            self.tool_combo.set("Aucun outil trouvé")

    def append_log(self, text: str):
        self.log_area.insert(tk.END, text)
        self.log_area.see(tk.END)

    def start_process(self):
        tool = self.tool_combo.get()
        if not tool or tool == "Aucun outil trouvé":
            messagebox.showwarning("Attention", "Veuillez d'abord placer un exécutable dans bin/ et le sélectionner.")
            return

        tool_path = os.path.join(BIN_DIR, tool)
        args = self.args_entry.get().strip().split() if self.args_entry.get().strip() else []
        cmd = [tool_path] + args

        self.log_area.delete("1.0", tk.END)
        self.append_log(f"> Exécution : {' '.join(cmd)}\n{'-'*50}\n")

        self.run_btn.config(state="disabled")
        self.stop_btn.config(state="normal")
        self.runner.run(cmd, cwd=BIN_DIR)

    def stop_process(self):
        self.runner.stop()
        self.append_log("\n[PROCESSUS ARRÊTÉ PAR L'UTILISATEUR]\n")
        self.on_process_finished(0)

    def on_process_finished(self, code: int):
        self.append_log(f"\n{'-'*50}\nTerminé avec le code de sortie : {code}\n")
        self.run_btn.config(state="normal")
        self.stop_btn.config(state="disabled")


if __name__ == "__main__":
    app = App()
    app.mainloop()
