from pathlib import Path
p=Path('atendimento.html')
s=p.read_text(encoding='utf-8')
old='''      const propostaResumo = document.getElementById("propostaResumo");\n      if (navAtencao) navAtencao.style.display = corporativo ? "none" : "";\n      if (navDisponibilidade) navDisponibilidade.style.display = corporativo ? "none" : "";\n      if (propostaResumo) propostaResumo.style.display = corporativo ? "none" : "";'''
new='''      const propostaResumo = document.getElementById("propostaResumo");\n      const bottomNav = document.querySelector(".bottom-nav");\n      if (navAtencao) navAtencao.style.display = corporativo ? "none" : "";\n      if (navDisponibilidade) navDisponibilidade.style.display = corporativo ? "none" : "";\n      if (propostaResumo) propostaResumo.style.display = corporativo ? "none" : "";\n      if (bottomNav) bottomNav.style.gridTemplateColumns = corporativo ? "repeat(3, 1fr)" : "repeat(5, 1fr)";'''
if old not in s: raise RuntimeError('marcador bottom nav nao encontrado')
s=s.replace(old,new,1)
p.write_text(s,encoding='utf-8')
print('ajuste V1.15b aplicado')
