# Generator for Jumanji educational website
import json

CSS = """
:root {
  --bg: #0d1a10;
  --bg2: #0a1a0f;
  --card: #112316;
  --card2: #162c1a;
  --border: #1e4d22;
  --gold: #c9a227;
  --gold2: #f0c040;
  --green: #4ade80;
  --green2: #22c55e;
  --text: #e8f5e9;
  --text2: #a7c8a9;
  --text3: #6b917a;
  --judy: #166534;
  --peter: #1e3a8a;
  --box: #7c2d12;
  --red: #ef4444;
  --shadow: rgba(0,0,0,0.5);
}
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }
body {
  font-family: 'Segoe UI', Arial, sans-serif;
  background: var(--bg);
  color: var(--text);
  min-height: 100vh;
  display: flex;
}

/* ─── NAV ─── */
.sidebar {
  width: 220px;
  min-height: 100vh;
  background: #061009;
  border-right: 1px solid var(--border);
  display: flex;
  flex-direction: column;
  position: fixed;
  top: 0; left: 0; bottom: 0;
  z-index: 100;
  padding: 0 0 20px 0;
}
.sidebar-logo {
  padding: 22px 20px 18px;
  border-bottom: 1px solid var(--border);
  cursor: pointer;
}
.sidebar-logo .logo-title {
  font-size: 1.3rem;
  font-weight: 900;
  color: var(--gold);
  letter-spacing: 2px;
  text-transform: uppercase;
}
.sidebar-logo .logo-sub {
  font-size: 0.7rem;
  color: var(--text3);
  margin-top: 2px;
  text-transform: uppercase;
  letter-spacing: 1px;
}
.nav-section {
  padding: 12px 14px 4px;
  font-size: 0.65rem;
  text-transform: uppercase;
  letter-spacing: 1.5px;
  color: var(--text3);
}
.nav-item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 9px 20px;
  font-size: 0.88rem;
  color: var(--text2);
  cursor: pointer;
  border-left: 3px solid transparent;
  transition: all 0.15s;
  text-decoration: none;
}
.nav-item:hover { background: var(--card); color: var(--text); border-left-color: var(--border); }
.nav-item.active { background: var(--card2); color: var(--green); border-left-color: var(--green); font-weight: 600; }
.nav-item .nav-emoji { font-size: 1rem; width: 20px; text-align: center; }
.nav-sub-item {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 6px 20px 6px 36px;
  font-size: 0.8rem;
  color: var(--text3);
  cursor: pointer;
  transition: all 0.15s;
}
.nav-sub-item:hover { color: var(--text2); }
.nav-sub-item.active { color: var(--green); }
.nav-divider { height: 1px; background: var(--border); margin: 8px 14px; }

/* ─── MAIN ─── */
#main {
  margin-left: 220px;
  flex: 1;
  min-height: 100vh;
  overflow-x: hidden;
}
.view { display: none; }
.view.active { display: block; }

/* ─── HOME ─── */
.hero {
  background: linear-gradient(135deg, #061009 0%, #0d2a12 50%, #0a1f0d 100%);
  min-height: 340px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: 60px 40px 50px;
  position: relative;
  overflow: hidden;
  border-bottom: 1px solid var(--border);
}
.hero::before {
  content: '';
  position: absolute; inset: 0;
  background:
    radial-gradient(ellipse at 20% 50%, rgba(201,162,39,0.05) 0%, transparent 60%),
    radial-gradient(ellipse at 80% 50%, rgba(74,222,128,0.04) 0%, transparent 60%);
}
.hero-badge {
  display: inline-block;
  background: rgba(201,162,39,0.12);
  border: 1px solid rgba(201,162,39,0.4);
  color: var(--gold);
  font-size: 0.7rem;
  font-weight: 700;
  letter-spacing: 2px;
  text-transform: uppercase;
  padding: 4px 14px;
  border-radius: 20px;
  margin-bottom: 16px;
}
.hero h1 {
  font-size: 3.5rem;
  font-weight: 900;
  color: var(--gold);
  letter-spacing: 4px;
  text-transform: uppercase;
  text-shadow: 0 0 40px rgba(201,162,39,0.3);
  margin-bottom: 8px;
}
.hero-sub {
  font-size: 1rem;
  color: var(--text2);
  letter-spacing: 1px;
  margin-bottom: 24px;
}
.hero-desc {
  max-width: 520px;
  font-size: 0.9rem;
  color: var(--text3);
  line-height: 1.7;
}
.home-grid {
  padding: 32px 32px;
}
.home-grid-title {
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 2px;
  color: var(--text3);
  margin-bottom: 16px;
  padding-left: 4px;
}
.seances-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 14px;
  margin-bottom: 32px;
}
.seance-card {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 18px 20px;
  cursor: pointer;
  transition: all 0.2s;
  position: relative;
  overflow: hidden;
}
.seance-card::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 3px;
}
.seance-card.judy::before { background: linear-gradient(90deg, #166534, #4ade80); }
.seance-card.peter::before { background: linear-gradient(90deg, #1e3a8a, #60a5fa); }
.seance-card.boite::before { background: linear-gradient(90deg, #7c2d12, #f97316); }
.seance-card:hover {
  border-color: rgba(201,162,39,0.5);
  background: var(--card2);
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(0,0,0,0.3);
}
.card-num {
  font-size: 0.65rem;
  text-transform: uppercase;
  letter-spacing: 1.5px;
  color: var(--text3);
  margin-bottom: 6px;
}
.card-emoji { font-size: 1.8rem; margin-bottom: 8px; display: block; }
.card-titre {
  font-size: 1rem;
  font-weight: 700;
  color: var(--text);
  margin-bottom: 3px;
}
.card-sous {
  font-size: 0.78rem;
  color: var(--text3);
  margin-bottom: 10px;
}
.card-perso {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  font-size: 0.72rem;
  font-weight: 600;
  padding: 3px 10px;
  border-radius: 20px;
}
.card-perso.judy { background: rgba(22,101,52,0.3); color: #4ade80; border: 1px solid rgba(74,222,128,0.3); }
.card-perso.peter { background: rgba(30,58,138,0.3); color: #93c5fd; border: 1px solid rgba(96,165,250,0.3); }
.card-perso.boite { background: rgba(124,45,18,0.3); color: #fb923c; border: 1px solid rgba(249,115,22,0.3); }
.card-video-badge {
  position: absolute;
  top: 14px; right: 14px;
  background: rgba(201,162,39,0.15);
  border: 1px solid rgba(201,162,39,0.3);
  color: var(--gold);
  font-size: 0.65rem;
  padding: 2px 7px;
  border-radius: 10px;
}

/* Quick access buttons */
.quick-access {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
  margin-top: 8px;
}
.qa-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 12px 20px;
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 10px;
  color: var(--text2);
  cursor: pointer;
  font-size: 0.88rem;
  transition: all 0.15s;
}
.qa-btn:hover { background: var(--card2); border-color: var(--gold); color: var(--gold); }

/* ─── SEANCE VIEW ─── */
.seance-page { max-width: 900px; margin: 0 auto; padding: 32px 32px 60px; }
.seance-back {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  color: var(--text3);
  font-size: 0.82rem;
  cursor: pointer;
  margin-bottom: 20px;
  padding: 5px 10px;
  border-radius: 6px;
  transition: all 0.15s;
}
.seance-back:hover { color: var(--text); background: var(--card); }
.seance-header {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 14px;
  padding: 24px 28px;
  margin-bottom: 24px;
}
.seance-header-top {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 16px;
  margin-bottom: 14px;
}
.seance-num-badge {
  font-size: 0.65rem;
  text-transform: uppercase;
  letter-spacing: 1.5px;
  color: var(--text3);
}
.seance-titre-main {
  font-size: 1.8rem;
  font-weight: 900;
  color: var(--gold);
  margin-top: 4px;
}
.seance-sous-titre {
  font-size: 0.95rem;
  color: var(--text2);
  margin-top: 2px;
}
.objectifs-list {
  display: flex;
  flex-direction: column;
  gap: 5px;
  margin-top: 12px;
}
.objectif-item {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 0.83rem;
  color: var(--text2);
}
.objectif-item::before {
  content: '';
  width: 6px; height: 6px;
  border-radius: 50%;
  background: var(--green);
  flex-shrink: 0;
}

/* ─── VIDEO PLAYER ─── */
.video-section {
  background: #000;
  border: 1px solid var(--border);
  border-radius: 14px;
  overflow: hidden;
  margin-bottom: 24px;
}
.video-section-header {
  background: var(--card);
  padding: 12px 20px;
  display: flex;
  align-items: center;
  gap: 10px;
  border-bottom: 1px solid var(--border);
}
.video-section-header .vh-badge {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  background: rgba(201,162,39,0.12);
  border: 1px solid rgba(201,162,39,0.3);
  color: var(--gold);
  font-size: 0.72rem;
  font-weight: 700;
  padding: 3px 10px;
  border-radius: 20px;
  text-transform: uppercase;
  letter-spacing: 1px;
}
.video-section-header .vh-title {
  font-size: 0.88rem;
  color: var(--text2);
}
.video-player {
  width: 100%;
  max-height: 480px;
  display: block;
  background: #000;
}
.video-script {
  background: var(--card);
  border-top: 1px solid var(--border);
  padding: 14px 20px;
}
.video-script-toggle {
  display: flex;
  align-items: center;
  justify-content: space-between;
  cursor: pointer;
  font-size: 0.82rem;
  color: var(--text3);
}
.video-script-toggle:hover { color: var(--text2); }
.video-script-content {
  display: none;
  margin-top: 10px;
  font-size: 0.85rem;
  color: var(--text2);
  line-height: 1.7;
  border-left: 3px solid var(--border);
  padding-left: 14px;
  font-style: italic;
}
.video-script-content.open { display: block; }
.video-placeholder {
  padding: 60px 20px;
  text-align: center;
  color: var(--text3);
}
.video-placeholder .vp-icon { font-size: 3rem; margin-bottom: 10px; }
.video-placeholder .vp-text { font-size: 0.88rem; }

/* ─── EXERCISES ─── */
.exercises-section { display: flex; flex-direction: column; gap: 20px; }
.exercise-card {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 14px;
  overflow: hidden;
}
.exercise-card-header {
  padding: 14px 20px;
  background: var(--card2);
  border-bottom: 1px solid var(--border);
  display: flex;
  align-items: center;
  gap: 10px;
}
.exercise-type-badge {
  font-size: 0.65rem;
  text-transform: uppercase;
  letter-spacing: 1px;
  font-weight: 700;
  padding: 2px 8px;
  border-radius: 10px;
}
.badge-relier { background: rgba(201,162,39,0.15); color: var(--gold); border: 1px solid rgba(201,162,39,0.3); }
.badge-qcm { background: rgba(30,58,138,0.3); color: #93c5fd; border: 1px solid rgba(96,165,250,0.25); }
.badge-vf { background: rgba(22,101,52,0.3); color: #4ade80; border: 1px solid rgba(74,222,128,0.25); }
.badge-ordre { background: rgba(124,45,18,0.3); color: #fb923c; border: 1px solid rgba(249,115,22,0.25); }
.exercise-title {
  font-size: 0.9rem;
  font-weight: 700;
  color: var(--text);
}
.exercise-body { padding: 20px; }
.exercise-consigne {
  font-size: 0.82rem;
  color: var(--text3);
  font-style: italic;
  margin-bottom: 16px;
  border-left: 3px solid var(--border);
  padding-left: 10px;
}

/* ─── RELIER EXERCISE ─── */
.relier-wrap {
  position: relative;
  user-select: none;
}
.relier-cols {
  display: flex;
  align-items: flex-start;
  gap: 0;
}
.relier-left-col, .relier-right-col {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.relier-mid {
  width: 80px;
  flex-shrink: 0;
  position: relative;
}
.relier-svg {
  position: absolute;
  top: 0; left: -40px;
  width: 160px;
  height: 400px;
  pointer-events: none;
  overflow: visible;
  z-index: 5;
}
.relier-item {
  padding: 10px 14px;
  background: var(--bg2);
  border: 2px solid var(--border);
  border-radius: 8px;
  cursor: pointer;
  font-size: 0.87rem;
  color: var(--text);
  transition: all 0.15s;
  position: relative;
  line-height: 1.4;
}
.relier-item:hover { border-color: rgba(201,162,39,0.5); background: var(--card2); }
.relier-item.selected {
  border-color: var(--gold);
  background: rgba(201,162,39,0.08);
  box-shadow: 0 0 0 3px rgba(201,162,39,0.15);
}
.relier-item.matched-ok {
  border-color: var(--green);
  background: rgba(74,222,128,0.06);
  cursor: default;
  color: var(--text2);
}
.relier-item.matched-ok:hover { transform: none; }
.relier-item.shake {
  animation: shakeAnim 0.4s ease;
  border-color: var(--red);
  background: rgba(239,68,68,0.06);
}
@keyframes shakeAnim {
  0%,100% { transform: translateX(0); }
  25% { transform: translateX(-6px); }
  75% { transform: translateX(6px); }
}
.relier-result {
  margin-top: 12px;
  font-size: 0.88rem;
  font-weight: 700;
  color: var(--green);
  text-align: center;
  min-height: 24px;
}

/* ─── QCM EXERCISE ─── */
.qcm-question {
  font-size: 0.95rem;
  font-weight: 700;
  color: var(--text);
  margin-bottom: 14px;
}
.qcm-options { display: flex; flex-direction: column; gap: 8px; }
.qcm-option {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 16px;
  background: var(--bg2);
  border: 2px solid var(--border);
  border-radius: 10px;
  cursor: pointer;
  font-size: 0.87rem;
  color: var(--text);
  transition: all 0.15s;
}
.qcm-option:hover { border-color: rgba(201,162,39,0.4); background: var(--card2); }
.qcm-option .opt-letter {
  width: 26px; height: 26px;
  border-radius: 50%;
  background: var(--card);
  border: 1px solid var(--border);
  display: flex; align-items: center; justify-content: center;
  font-size: 0.72rem;
  font-weight: 700;
  flex-shrink: 0;
}
.qcm-option.correct { border-color: var(--green); background: rgba(74,222,128,0.08); }
.qcm-option.correct .opt-letter { background: var(--green); color: #000; border-color: var(--green); }
.qcm-option.wrong { border-color: var(--red); background: rgba(239,68,68,0.06); }
.qcm-option.wrong .opt-letter { background: var(--red); color: #fff; border-color: var(--red); }
.qcm-option.debate { border-color: rgba(201,162,39,0.5); cursor: pointer; }
.qcm-option.debate:hover { background: rgba(201,162,39,0.08); }
.qcm-option.debate-selected { border-color: var(--gold); background: rgba(201,162,39,0.1); }
.qcm-option.debate-selected .opt-letter { background: var(--gold); color: #000; }
.qcm-feedback {
  margin-top: 12px;
  padding: 10px 14px;
  background: rgba(74,222,128,0.06);
  border: 1px solid rgba(74,222,128,0.2);
  border-radius: 8px;
  font-size: 0.83rem;
  color: var(--text2);
  display: none;
}
.qcm-feedback.visible { display: block; }

/* ─── VRAI/FAUX EXERCISE ─── */
.vf-list { display: flex; flex-direction: column; gap: 10px; }
.vf-item {
  background: var(--bg2);
  border: 1px solid var(--border);
  border-radius: 10px;
  overflow: hidden;
}
.vf-statement {
  padding: 12px 16px;
  font-size: 0.87rem;
  color: var(--text);
  display: flex;
  align-items: flex-start;
  gap: 10px;
}
.vf-num {
  font-size: 0.72rem;
  color: var(--text3);
  font-weight: 700;
  flex-shrink: 0;
  margin-top: 2px;
}
.vf-buttons {
  display: flex;
  border-top: 1px solid var(--border);
}
.vf-btn {
  flex: 1;
  padding: 8px;
  text-align: center;
  cursor: pointer;
  font-size: 0.82rem;
  font-weight: 700;
  transition: all 0.15s;
}
.vf-btn-v { color: #4ade80; }
.vf-btn-v:hover { background: rgba(74,222,128,0.08); }
.vf-btn-f { color: #f87171; border-left: 1px solid var(--border); }
.vf-btn-f:hover { background: rgba(239,68,68,0.06); }
.vf-btn.active-ok { background: rgba(74,222,128,0.15); color: #4ade80; }
.vf-btn.active-wrong { background: rgba(239,68,68,0.1); color: #f87171; }
.vf-explication {
  padding: 8px 16px;
  font-size: 0.79rem;
  font-style: italic;
  color: var(--text3);
  display: none;
  border-top: 1px solid var(--border);
}
.vf-explication.visible { display: block; }
.vf-item.correct .vf-explication { color: #4ade80; }
.vf-item.wrong-ans .vf-explication { color: #f87171; }

/* ─── ORDRE EXERCISE ─── */
.ordre-list { display: flex; flex-direction: column; gap: 8px; }
.ordre-item {
  display: flex;
  align-items: center;
  gap: 10px;
  background: var(--bg2);
  border: 2px solid var(--border);
  border-radius: 10px;
  padding: 10px 14px;
  font-size: 0.87rem;
  color: var(--text);
  transition: border-color 0.15s;
}
.ordre-item.correct-pos { border-color: var(--green); }
.ordre-item-emoji { font-size: 1.2rem; flex-shrink: 0; }
.ordre-item-text { flex: 1; }
.ordre-moves { display: flex; gap: 4px; flex-shrink: 0; }
.ordre-btn {
  width: 28px; height: 28px;
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 5px;
  cursor: pointer;
  color: var(--text2);
  font-size: 0.8rem;
  display: flex; align-items: center; justify-content: center;
  transition: all 0.1s;
}
.ordre-btn:hover { background: var(--card2); color: var(--text); }
.ordre-btn:disabled { opacity: 0.3; cursor: default; }
.ordre-check {
  margin-top: 12px;
  display: flex;
  gap: 10px;
  align-items: center;
}
.btn-check {
  padding: 8px 18px;
  background: rgba(201,162,39,0.1);
  border: 1px solid rgba(201,162,39,0.4);
  color: var(--gold);
  border-radius: 8px;
  cursor: pointer;
  font-size: 0.82rem;
  font-weight: 700;
  transition: all 0.15s;
}
.btn-check:hover { background: rgba(201,162,39,0.18); }
.ordre-result { font-size: 0.83rem; color: var(--text3); }

/* ─── DICTÉES VIEW ─── */
.page-header-bar {
  padding: 28px 32px 20px;
  border-bottom: 1px solid var(--border);
}
.page-header-bar h2 {
  font-size: 1.6rem;
  font-weight: 900;
  color: var(--gold);
  margin-bottom: 4px;
}
.page-header-bar p {
  font-size: 0.85rem;
  color: var(--text3);
}
.dictees-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
  gap: 14px;
  padding: 24px 32px;
}
.dictee-card {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 16px 18px;
  cursor: pointer;
  transition: all 0.2s;
}
.dictee-card:hover {
  border-color: rgba(201,162,39,0.4);
  background: var(--card2);
  transform: translateY(-2px);
}
.dictee-type-badge {
  display: inline-block;
  font-size: 0.65rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1px;
  padding: 2px 8px;
  border-radius: 10px;
  margin-bottom: 8px;
}
.tb-flash { background: rgba(123,31,162,0.3); color: #d8b4fe; border: 1px solid rgba(168,85,247,0.3); }
.tb-trous { background: rgba(21,101,192,0.3); color: #93c5fd; border: 1px solid rgba(59,130,246,0.3); }
.tb-coeur { background: rgba(0,105,92,0.3); color: #6ee7b7; border: 1px solid rgba(52,211,153,0.3); }
.tb-neg { background: rgba(230,81,0,0.3); color: #fdba74; border: 1px solid rgba(249,115,22,0.3); }
.dictee-num { font-size: 1rem; font-weight: 900; color: var(--text); margin-bottom: 2px; }
.dictee-sous { font-size: 0.78rem; color: var(--text3); }
.dictee-links { margin-top: 14px; display: flex; gap: 8px; flex-wrap: wrap; }
.dictee-link-btn {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  padding: 5px 11px;
  font-size: 0.75rem;
  font-weight: 600;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.15s;
  text-decoration: none;
}
.dlb-eleve { background: rgba(30,58,138,0.3); border: 1px solid rgba(96,165,250,0.3); color: #93c5fd; }
.dlb-eleve:hover { background: rgba(30,58,138,0.5); }
.dlb-prof { background: rgba(124,45,18,0.3); border: 1px solid rgba(249,115,22,0.3); color: #fdba74; }
.dlb-prof:hover { background: rgba(124,45,18,0.5); }

/* ─── ENSEIGNANT VIEW ─── */
.enseignant-content { padding: 24px 32px 60px; max-width: 900px; }
.ens-section { margin-bottom: 28px; }
.ens-section-title {
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 2px;
  color: var(--gold);
  margin-bottom: 12px;
  padding-bottom: 6px;
  border-bottom: 1px solid var(--border);
}
.ens-cards { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
.ens-card {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 14px 16px;
  cursor: pointer;
  transition: all 0.15s;
  text-decoration: none;
  display: block;
}
.ens-card:hover { border-color: rgba(201,162,39,0.4); background: var(--card2); }
.ens-card-icon { font-size: 1.5rem; margin-bottom: 6px; }
.ens-card-title { font-size: 0.88rem; font-weight: 700; color: var(--text); margin-bottom: 2px; }
.ens-card-desc { font-size: 0.76rem; color: var(--text3); }
.script-block {
  background: var(--bg2);
  border: 1px solid var(--border);
  border-radius: 10px;
  margin-bottom: 12px;
  overflow: hidden;
}
.script-block-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px 16px;
  background: var(--card);
  border-bottom: 1px solid var(--border);
  cursor: pointer;
}
.script-block-header:hover { background: var(--card2); }
.script-block-num { font-size: 0.82rem; font-weight: 700; color: var(--gold); }
.script-block-titre { font-size: 0.82rem; color: var(--text2); }
.script-block-body {
  padding: 14px 16px;
  font-size: 0.83rem;
  color: var(--text2);
  line-height: 1.75;
  font-style: italic;
  display: none;
}
.script-block-body.open { display: block; }

/* ─── GRAMMAIRE VIEW ─── */
.grammaire-iframe-wrap { height: calc(100vh - 0px); }
.grammaire-iframe { width: 100%; height: 100%; border: none; }

/* ─── PROGRESS BAR ─── */
.progress-bar-wrap { margin-top: 16px; }
.progress-bar-label { font-size: 0.72rem; color: var(--text3); margin-bottom: 5px; display: flex; justify-content: space-between; }
.progress-bar { height: 4px; background: var(--border); border-radius: 2px; overflow: hidden; }
.progress-bar-fill { height: 100%; background: var(--green); border-radius: 2px; transition: width 0.5s; }

/* ─── RESPONSIVE ─── */
@media (max-width: 760px) {
  .sidebar { width: 54px; }
  .sidebar-logo .logo-title, .nav-item span, .nav-section { display: none; }
  .nav-item { padding: 12px; justify-content: center; }
  #main { margin-left: 54px; }
  .hero h1 { font-size: 2rem; }
  .ens-cards { grid-template-columns: 1fr; }
}
"""

# Séances data
SEANCES = [
  {
    "id": 1,
    "titre": "Découverte",
    "sous_titre": "Observation de la couverture",
    "personnage": "judy",
    "emoji": "🌿",
    "video": "Vidéos Judy/Judy_Jumanji_séance_1.mp4",
    "script": "Bonjour ! Je m'appelle Judy. Aujourd'hui, je voudrais vous parler d'un jeu… un jeu pas comme les autres. Je l'ai trouvé un après-midi dans le parc, mon frère Peter et moi. Une vieille boîte, abandonnée sous un arbre. Dessus, il y avait écrit… JUMANJI. Avant qu'on commence à lire ensemble, j'ai une question pour vous : quand vous voyez la couverture de ce livre… qu'est-ce que vous imaginez ? Une aventure ? Un danger ? Quelque chose de magique ? On se retrouve bientôt pour commencer l'aventure… si vous êtes prêts !",
    "objectifs": [
      "Observer les éléments d'une couverture d'album",
      "Formuler des hypothèses de lecture",
      "Comprendre le vocabulaire de l'œuvre"
    ],
    "exercises": [
      {
        "type": "relier",
        "titre": "Vocabulaire — Relie chaque mot à sa définition",
        "consigne": "Clique d'abord sur un mot à gauche (il s'illumine en or), puis clique sur sa définition à droite pour tracer le lien.",
        "pairs": [
          {"left": "abandonné", "right": "laissé sans s'en occuper"},
          {"left": "mystérieux", "right": "étrange, difficile à expliquer"},
          {"left": "courageux", "right": "qui n'a pas peur du danger"},
          {"left": "avertissement", "right": "message qui prévient d'un danger"},
          {"left": "plateau de jeu", "right": "surface plate avec des cases pour jouer"}
        ]
      },
      {
        "type": "qcm",
        "titre": "Genre littéraire — Quel est le genre de cet album ?",
        "question": "D'après la couverture et le début de l'histoire, cet album appartient au genre :",
        "debate": False,
        "options": [
          {"text": "Une histoire d'amour", "correct": False},
          {"text": "Une aventure fantastique", "correct": True},
          {"text": "Un conte de fées classique", "correct": False},
          {"text": "Une histoire policière", "correct": False}
        ],
        "feedback": "C'est une aventure fantastique ! Le jeu Jumanji fait apparaître des animaux réels et dangereux dans la maison — c'est le propre du fantastique : le merveilleux envahit le quotidien."
      }
    ]
  },
  {
    "id": 2,
    "titre": "Questionnaire 1",
    "sous_titre": "Entrée dans l'histoire",
    "personnage": "judy",
    "emoji": "📖",
    "video": "Vidéos Judy/Judy_Jumanji_séance_2.mp4",
    "script": "Bonjour, c'est encore moi, Judy ! Lors de notre dernière séance, vous avez observé la couverture et imaginé ce qui allait se passer. Aujourd'hui, on commence vraiment l'histoire. Ce jour-là, Peter et moi, on s'ennuyait. Nos parents étaient sortis. C'est là qu'on a trouvé la boîte. Elle était posée là, comme si elle nous attendait. Sur le couvercle, une note disait : Jeu de plateau de la jungle pour enfants courageux. Une fois commencé, le jeu doit être terminé. Après avoir lu les pages d'aujourd'hui, notez dans votre cahier : qui sont les personnages, où se passe l'histoire, et ce que vous pensez qu'il va arriver.",
    "objectifs": [
      "Identifier les personnages et leurs caractéristiques",
      "Comprendre la situation initiale du récit",
      "Formuler des prédictions sur la suite"
    ],
    "exercises": [
      {
        "type": "relier",
        "titre": "Les personnages — Relie chaque élément à la bonne description",
        "consigne": "Clique sur un élément à gauche, puis sur sa description à droite.",
        "pairs": [
          {"left": "👧 Judy", "right": "Meneuse, sûre d'elle, prend les décisions"},
          {"left": "👦 Peter", "right": "Hésitant, a peur, suit sa sœur"},
          {"left": "📦 La boîte", "right": "Objet mystérieux trouvé dans le parc"},
          {"left": "🎲 Le jeu", "right": "Ne peut pas être arrêté une fois commencé"},
          {"left": "🌳 Le parc", "right": "Endroit où les enfants découvrent la boîte"}
        ]
      },
      {
        "type": "vf",
        "titre": "Vrai ou Faux ? — Compréhension de la situation initiale",
        "consigne": "Lis chaque affirmation. Clique sur VRAI ou FAUX, puis lis l'explication.",
        "items": [
          {"s": "Les enfants trouvent le jeu dans leur chambre.", "ok": False, "exp": "Non ! Ils le trouvent dans le parc du quartier, sous un arbre."},
          {"s": "La règle dit que le jeu doit être terminé une fois commencé.", "ok": True, "exp": "Exact ! C'est l'avertissement crucial sur la boîte."},
          {"s": "Peter est le plus courageux des deux enfants.", "ok": False, "exp": "Non. C'est Judy qui est la meneuse. Peter est hésitant et suit sa sœur."},
          {"s": "Un lion apparaît dès le premier lancer de dés.", "ok": True, "exp": "Oui ! Peter lance les dés, avance sa pièce, et un lion surgit dans la maison."}
        ]
      }
    ]
  },
  {
    "id": 3,
    "titre": "Causes & Effets",
    "sous_titre": "Les premiers dangers",
    "personnage": "peter",
    "emoji": "🦁",
    "video": "Vidéos Judy/Peter_Jumanji_séance_3.mp4",
    "script": "Euh… bonjour. Je m'appelle Peter. C'est Judy qui m'a demandé de vous expliquer ce qui s'est passé. Mais c'est pas facile à raconter… parce que moi-même, j'y crois encore à moitié. La dernière fois, vous avez vu comment on a trouvé la boîte. Le jeu Jumanji. On a décidé de jouer. Et là… C'est moi qui ai lancé les dés en premier. J'ai avancé ma pièce. J'ai lu la case : Un lion cherche son repas, reculez de deux cases. Et j'ai entendu quelque chose. Un grondement. Du haut de l'escalier. Un vrai lion nous regardait. Le jeu doit être terminé. Pendant la lecture, cherchez à chaque fois : quelle est la case ? Et qu'est-ce qui se passe dans la maison juste après ? Cause et effet.",
    "objectifs": [
      "Identifier les relations cause → effet dans le récit",
      "Comprendre la logique du jeu Jumanji",
      "Relever les événements dans l'ordre"
    ],
    "exercises": [
      {
        "type": "relier",
        "titre": "Cause → Effet — Relie chaque case du jeu à ce qu'elle provoque",
        "consigne": "Clique sur une case du jeu à gauche, puis sur l'effet provoqué à droite.",
        "pairs": [
          {"left": "🎲 « Un lion cherche son repas »", "right": "Un lion surgit en haut de l'escalier"},
          {"left": "🎲 « Troupe de singes affamés »", "right": "Des singes envahissent la cuisine"},
          {"left": "🎲 « Mousson dans le salon »", "right": "Il pleut à l'intérieur de la maison"},
          {"left": "🎲 « Rhinocéros en liberté »", "right": "Un rhinocéros charge à travers les murs"},
          {"left": "🏆 Crier « JUMANJI ! »", "right": "Tout disparaît comme par magie"}
        ]
      },
      {
        "type": "qcm",
        "titre": "Compréhension — Pourquoi les enfants ne peuvent-ils pas s'arrêter ?",
        "question": "Quelle règle les empêche d'abandonner la partie en cours ?",
        "debate": False,
        "options": [
          {"text": "Ils ont peur d'être punis par leurs parents.", "correct": False},
          {"text": "La règle dit : « Une fois commencé, le jeu doit être terminé. »", "correct": True},
          {"text": "Ils adorent jouer et ne veulent pas s'arrêter.", "correct": False},
          {"text": "Le lion les empêche physiquement de s'enfuir.", "correct": False}
        ],
        "feedback": "Exactement ! La règle inscrite sur la boîte est claire : le jeu DOIT être terminé. C'est ce qui crée toute la tension du récit."
      }
    ]
  },
  {
    "id": 4,
    "titre": "Frise chronologique",
    "sous_titre": "Les dangers dans l'ordre",
    "personnage": "peter",
    "emoji": "📅",
    "video": "Vidéos Judy/Peter_Jumanji_séance_4.mp4",
    "script": "Euh, bonjour, c'est encore Peter. Un lion… un rhinocéros… une mousson dans le salon… vous commencez à voir le problème, non ? Judy dit qu'il faut rester calme et chercher la logique. Moi, j'étais surtout en train d'essayer de ne pas paniquer. Mais elle a raison sur un truc : chaque case fait apparaître quelque chose. Et on peut pas s'arrêter. Aujourd'hui, vous allez construire la frise des dangers. Dans l'ordre. Chaque danger, un après l'autre. Et j'ai une question que je me pose : est-ce que ce jeu est juste ? Est-ce que les dangers sont proportionnels ? Peut-être que vous, vous y arriverez.",
    "objectifs": [
      "Remettre les événements dans l'ordre chronologique",
      "Comprendre la structure narrative (escalade des dangers)",
      "Réfléchir aux choix de l'auteur"
    ],
    "exercises": [
      {
        "type": "ordre",
        "titre": "Remets les événements dans l'ordre chronologique",
        "consigne": "Utilise les flèches ↑ ↓ pour déplacer chaque événement à sa bonne place dans l'histoire.",
        "items": [
          {"text": "Les enfants trouvent une boîte mystérieuse dans le parc", "pos": 1, "emoji": "📦"},
          {"text": "Ils rentrent à la maison et ouvrent la boîte", "pos": 2, "emoji": "🏠"},
          {"text": "Peter lance les dés pour la première fois", "pos": 3, "emoji": "🎲"},
          {"text": "Un lion surgit en haut de l'escalier", "pos": 4, "emoji": "🦁"},
          {"text": "Des singes envahissent la cuisine", "pos": 5, "emoji": "🐒"},
          {"text": "Un rhinocéros charge à travers la maison", "pos": 6, "emoji": "🦏"},
          {"text": "Il pleut à l'intérieur du salon (mousson)", "pos": 7, "emoji": "🌧️"},
          {"text": "Judy crie « JUMANJI ! » et tout disparaît", "pos": 8, "emoji": "🎉"}
        ]
      }
    ]
  },
  {
    "id": 5,
    "titre": "Schéma narratif",
    "sous_titre": "La fin de l'aventure",
    "personnage": "peter",
    "emoji": "🗺️",
    "video": "Vidéos Judy/Peter_Jumanji_séance_5.mp4",
    "script": "Bonjour. C'est Peter. Et… on y est. La fin. Je vais pas vous mentir : au début de cette aventure, j'étais terrifié. Mais Judy et moi, on a continué. Et quand j'ai enfin pu crier Jumanji… tout s'est arrêté. La jungle a disparu. La maison était comme avant. À la toute dernière page, on a regardé par la fenêtre. Et on a vu deux garçons qui couraient dans le parc. Avec une boîte sous le bras. Vous avez compris ce que ça veut dire ? Après la lecture, complétez le schéma narratif complet.",
    "objectifs": [
      "Identifier les étapes du schéma narratif",
      "Comprendre la chute de l'histoire",
      "Réfléchir au message de l'auteur"
    ],
    "exercises": [
      {
        "type": "relier",
        "titre": "Schéma narratif — Relie chaque étape à ce qui la décrit",
        "consigne": "Clique sur une étape du schéma à gauche, puis sur sa description à droite.",
        "pairs": [
          {"left": "📍 Situation initiale", "right": "Judy et Peter s'ennuient. Ils vont au parc."},
          {"left": "⚡ Élément déclencheur", "right": "Ils trouvent la boîte et décident de jouer."},
          {"left": "🌊 Péripéties", "right": "Les animaux envahissent la maison un par un."},
          {"left": "✅ Résolution", "right": "Judy crie « JUMANJI ! » — tout disparaît."},
          {"left": "🔄 Situation finale", "right": "Danny et Walter ramassent la boîte dans le parc."}
        ]
      },
      {
        "type": "vf",
        "titre": "La chute — Vrai ou Faux ?",
        "consigne": "Réponds sur les événements de la fin de l'histoire.",
        "items": [
          {"s": "À la fin, la maison est complètement détruite.", "ok": False, "exp": "Non ! Tout disparaît comme par magie quand Judy crie JUMANJI. La maison retrouve son état normal."},
          {"s": "Danny et Walter trouvent la boîte à la fin de l'histoire.", "ok": True, "exp": "Oui ! Ce sont eux qui ramassent la boîte dans le parc — une nouvelle partie va commencer."},
          {"s": "Les parents remarquent ce qui s'est passé dans la maison.", "ok": False, "exp": "Non ! Les parents rentrent et trouvent la maison comme avant. Ils ne savent rien."},
          {"s": "La fin suggère que l'aventure va se répéter.", "ok": True, "exp": "Exactement ! C'est la chute inquiétante : le jeu ne s'arrête jamais vraiment."}
        ]
      }
    ]
  },
  {
    "id": 6,
    "titre": "Débat interprétatif",
    "sous_titre": "On réfléchit ensemble",
    "personnage": "judy",
    "emoji": "💬",
    "video": "Vidéos Judy/Judy_Jumanji_séance_6.mp4",
    "script": "Bonjour ! Aujourd'hui, pas de nouvelle lecture. Aujourd'hui, on réfléchit. Est-ce que Peter et moi, on a eu tort de jouer à Jumanji ? Est-ce qu'on est responsables de ce qui s'est passé dans la maison ? Et ce jeu… c'est vraiment un jeu ? Ou c'est autre chose ? Moi, j'ai mon avis. Mais ce qui m'intéresse, c'est le vôtre. Pour répondre, vous devez vous appuyer sur le texte. Pas juste « je pense que… » mais « dans le livre, il est écrit que… » C'est ça, interpréter une œuvre. Je vous fais confiance !",
    "objectifs": [
      "Interpréter une œuvre littéraire",
      "Argumenter avec des preuves du texte",
      "Développer et défendre un point de vue"
    ],
    "exercises": [
      {
        "type": "relier",
        "titre": "Arguments — Relie chaque argument à la position qu'il défend",
        "consigne": "Clique sur un argument à gauche, puis sur la position qu'il soutient à droite.",
        "pairs": [
          {"left": "« La règle dit qu'on doit finir le jeu. »", "right": "Les enfants n'avaient pas le choix"},
          {"left": "« Ils ont choisi d'ouvrir la boîte. »", "right": "Les enfants sont responsables"},
          {"left": "« Le jeu fait apparaître de vrais animaux. »", "right": "Jumanji n'est pas un vrai jeu"},
          {"left": "« Il y a des cases, des pions, des dés. »", "right": "Jumanji est bien un jeu"},
          {"left": "« Les animaux disparaissent comme par magie. »", "right": "L'histoire n'est pas réelle"}
        ]
      },
      {
        "type": "qcm",
        "titre": "Débat — Prends position !",
        "question": "Judy et Peter ont-ils eu tort de jouer à Jumanji ?",
        "debate": True,
        "options": [
          {"text": "Oui, ils auraient dû poser la boîte et partir.", "correct": None},
          {"text": "Non, ils ne pouvaient pas savoir ce qui allait arriver.", "correct": None},
          {"text": "Les deux : ils ont choisi, mais la règle les a piégés.", "correct": None}
        ],
        "feedback": "Il n'y a pas de bonne ou mauvaise réponse ! Ce qui compte : avoir un argument du texte pour défendre ta position. C'est ça, interpréter !"
      }
    ]
  },
  {
    "id": 7,
    "titre": "Les illustrations",
    "sous_titre": "Texte et image",
    "personnage": "boite",
    "emoji": "🖼️",
    "video": "Agent_video_Pippit_20260420233407.mp4",
    "script": "[son de jungle, grondement lointain] Je suis Jumanji. Vous pensiez que l'aventure était terminée ? Elle ne l'est jamais vraiment. Aujourd'hui, je veux attirer votre attention sur quelque chose que vous avez peut-être oublié de regarder… vraiment regarder. Les images. Chris Van Allsburg n'est pas seulement l'auteur de cette histoire. Il en est aussi l'illustrateur. Chaque ombre, chaque angle, chaque regard… il les a choisis. Aujourd'hui, vous allez jouer les détectives de l'image. Regardez bien. Dans Jumanji, rien n'est laissé au hasard.",
    "objectifs": [
      "Analyser les relations texte-image dans un album",
      "Identifier ce que l'image ajoute au texte",
      "Comprendre les choix artistiques de l'illustrateur"
    ],
    "exercises": [
      {
        "type": "relier",
        "titre": "Texte ou Image ? — Relie chaque information à sa source",
        "consigne": "Clique sur une information à gauche, puis sur sa source à droite (le texte ou l'image).",
        "pairs": [
          {"left": "🦁 Le lion est en haut de l'escalier", "right": "Le texte le dit"},
          {"left": "🦷 Le lion montre ses griffes et sa gueule", "right": "L'image le montre"},
          {"left": "🎲 Peter et Judy lancent les dés", "right": "Le texte le dit"},
          {"left": "📐 La pièce semble rétrécir autour des enfants", "right": "L'image le montre"},
          {"left": "📜 La règle : le jeu doit être terminé", "right": "Le texte le dit"}
        ]
      },
      {
        "type": "vf",
        "titre": "Rôle des illustrations — Vrai ou Faux ?",
        "consigne": "Réponds sur le rôle des illustrations dans cet album.",
        "items": [
          {"s": "Les illustrations répètent exactement ce que dit le texte.", "ok": False, "exp": "Non ! Elles ajoutent des détails, des émotions, une atmosphère que le texte n'exprime pas."},
          {"s": "Chris Van Allsburg est à la fois l'auteur et l'illustrateur.", "ok": True, "exp": "Oui ! Il a tout créé. Chaque choix visuel est donc parfaitement intentionnel."},
          {"s": "Les illustrations renforcent la peur et la tension du récit.", "ok": True, "exp": "Exactement ! Les angles, les ombres et les regards créent une atmosphère inquiétante unique."},
          {"s": "On comprendrait exactement la même histoire sans les images.", "ok": False, "exp": "Non ! Les images ajoutent des informations essentielles — l'album n'est pas pensé sans elles."}
        ]
      }
    ]
  },
  {
    "id": 8,
    "titre": "Évaluation finale",
    "sous_titre": "Le dernier jet de dés",
    "personnage": "boite",
    "emoji": "⭐",
    "video": None,
    "script": "[son de jungle, lointain] Je suis Jumanji. Vous avez fait un long chemin. Vous avez suivi Judy et Peter. Vous avez vu la jungle envahir leur maison. Maintenant… il est temps de voir ce que vous avez vraiment retenu. Ne craignez pas cette évaluation. C'est simplement le dernier jet de dés. Lisez attentivement. Prenez votre temps. Et n'oubliez pas… Jumanji attend toujours le prochain joueur.",
    "objectifs": [
      "Vérifier la compréhension globale de l'album",
      "Répondre à des questions de compréhension fine",
      "Exprimer son point de vue sur l'œuvre"
    ],
    "exercises": [
      {
        "type": "qcm",
        "titre": "Question 1 — Où les enfants trouvent-ils le jeu ?",
        "question": "Où Judy et Peter trouvent-ils la boîte de Jumanji ?",
        "debate": False,
        "options": [
          {"text": "Dans la cave de leur maison", "correct": False},
          {"text": "Dans un magasin de jouets", "correct": False},
          {"text": "Dans le parc du quartier, sous un arbre", "correct": True},
          {"text": "Dans le grenier de leurs grands-parents", "correct": False}
        ],
        "feedback": "La boîte était abandonnée sous un arbre dans le parc. C'est là que tout commence."
      },
      {
        "type": "vf",
        "titre": "Évaluation — Compréhension fine",
        "consigne": "Réponds à ces questions de compréhension sur l'ensemble de l'album.",
        "items": [
          {"s": "Le titre JUMANJI est écrit en lettres dorées sur la boîte.", "ok": True, "exp": "Exact ! Les lettres dorées forment le titre mystérieux sur le couvercle."},
          {"s": "Les parents sont à la maison pendant toute la partie.", "ok": False, "exp": "Non ! Les parents sont sortis. C'est pour ça que les enfants s'ennuient et vont au parc."},
          {"s": "Peter est le premier à crier « JUMANJI ! »", "ok": False, "exp": "Non ! C'est Judy qui crie JUMANJI et met fin à la partie."},
          {"s": "À la fin, deux nouveaux enfants ramassent la boîte.", "ok": True, "exp": "Oui ! Danny et Walter — et ils courent, ce qui suggère qu'ils connaissent peut-être déjà le jeu…"}
        ]
      }
    ]
  }
]

DICTEES = [
  {"num": "J·1", "type": "flash", "titre": "La boîte abandonnée", "sem": "Sem.1 · Mardi 5 mai", "notions": "Majuscules, ponctuation, guillemets"},
  {"num": "J·2", "type": "trous", "titre": "La découverte du jeu", "sem": "Sem.1 · Jeudi 7 mai", "notions": "Déterminants, accord nom-adjectif"},
  {"num": "J·3", "type": "flash", "titre": "Le lion dans le salon", "sem": "Sem.2 · Lundi 11 mai", "notions": "Accord COD, terminaisons passé simple"},
  {"num": "J·4", "type": "trous", "titre": "Le salon dévasté", "sem": "Sem.2 · Mardi 12 mai", "notions": "Constituants du GN (det + nom + adj)"},
  {"num": "J·5", "type": "neg", "titre": "Les singes du plafond", "sem": "Sem.2 · Vendredi 15 mai", "notions": "Passé simple, adjectifs attributs"},
  {"num": "J·6", "type": "coeur", "titre": "La fin du jeu", "sem": "Sem.3 · Lundi 18 mai", "notions": "Ponctuation discours, adjectifs épithètes"},
  {"num": "J·7", "type": "trous", "titre": "Judy lance les dés", "sem": "Sem.3 · Mardi 19 mai", "notions": "COD et COI"},
  {"num": "J·8", "type": "coeur", "titre": "La chute de l'histoire", "sem": "Sem.4 · Lundi 25 mai", "notions": "Dialogue (guillemets, tirets)"},
  {"num": "J·9", "type": "flash", "titre": "Le rhinocéros surgit", "sem": "Sem.4 · Mardi 26 mai", "notions": "CC de lieu, temps, manière"},
  {"num": "J·10", "type": "neg", "titre": "Le jeu terminé", "sem": "Sem.4 · Vendredi 29 mai", "notions": "Accord participe passé avec avoir"}
]

SCRIPTS = [
  {
    "num": "Séance 1", "perso": "Judy", "outil": "HeyGen", "classe": "judy",
    "titre": "Découverte — Observation de la couverture",
    "texte": "Bonjour ! Je m'appelle Judy. Aujourd'hui, je voudrais vous parler d'un jeu… un jeu pas comme les autres. Je l'ai trouvé un après-midi dans le parc, mon frère Peter et moi. Une vieille boîte, abandonnée sous un arbre. Dessus, il y avait écrit… Jumanji. Avant qu'on commence à lire ensemble, j'ai une question pour vous : quand vous voyez la couverture de ce livre… qu'est-ce que vous imaginez ? Prenez le temps d'observer chaque détail. Les images, c'est important dans cet album. On se retrouve bientôt pour commencer l'aventure… si vous êtes prêts !"
  },
  {
    "num": "Séance 2", "perso": "Judy", "outil": "HeyGen", "classe": "judy",
    "titre": "Questionnaire 1 — Entrée dans l'histoire",
    "texte": "Bonjour, c'est encore moi, Judy ! Aujourd'hui, on commence vraiment l'histoire. Ce jour-là, Peter et moi, on s'ennuyait. C'est là qu'on a trouvé la boîte. Elle était posée là, comme si elle nous attendait. Sur le couvercle, une note disait : Jeu de plateau de la jungle pour enfants courageux. Une fois commencé, le jeu doit être terminé. Des enfants courageux… vous pensez qu'on aurait dû continuer ? Ou poser la boîte et partir ?"
  },
  {
    "num": "Séance 3", "perso": "Peter", "outil": "D-ID", "classe": "peter",
    "titre": "Questionnaire 2 — Cause et effet",
    "texte": "Euh… bonjour. Je m'appelle Peter. C'est Judy qui m'a demandé de vous expliquer ce qui s'est passé. La dernière fois, vous avez vu comment on a trouvé la boîte. Le jeu Jumanji. On a décidé de jouer. Et là… C'est moi qui ai lancé les dés en premier. J'ai avancé ma pièce. J'ai lu la case : Un lion cherche son repas. Et j'ai entendu quelque chose. Un grondement. Du haut de l'escalier. Un vrai lion nous regardait."
  },
  {
    "num": "Séance 4", "perso": "Peter", "outil": "D-ID", "classe": "peter",
    "titre": "Frise chronologique — Les dangers dans l'ordre",
    "texte": "Euh, bonjour, c'est encore Peter. Un lion… un rhinocéros… une mousson dans le salon… vous commencez à voir le problème, non ? Judy, elle dit qu'il faut rester calme. Aujourd'hui, vous allez construire la frise des dangers. Dans l'ordre. Et j'ai une question : est-ce que ce jeu est juste ? J'ai essayé de comprendre… je suis pas sûr d'avoir trouvé la réponse."
  },
  {
    "num": "Séance 5", "perso": "Peter", "outil": "D-ID", "classe": "peter",
    "titre": "Questionnaire 3 — Schéma narratif",
    "texte": "Bonjour. C'est Peter. Et… on y est. La fin. Au début, j'étais terrifié. Mais Judy et moi, on a continué. Et quand j'ai enfin pu crier Jumanji… tout s'est arrêté. La jungle a disparu. Enfin… presque. À la toute dernière page, on a regardé par la fenêtre. Et on a vu deux garçons qui couraient dans le parc. Avec une boîte sous le bras."
  },
  {
    "num": "Séance 6", "perso": "Judy", "outil": "HeyGen", "classe": "judy",
    "titre": "Débat interprétatif",
    "texte": "Bonjour ! Aujourd'hui, pas de nouvelle lecture. Aujourd'hui, on réfléchit. Est-ce que Peter et moi, on a eu tort de jouer à Jumanji ? Et ce jeu… c'est vraiment un jeu ? Moi, j'ai mon avis. Mais ce qui m'intéresse, c'est le vôtre. Pour répondre, vous devez vous appuyer sur le texte. Pas juste « je pense que… » mais « dans le livre, il est écrit que… »"
  },
  {
    "num": "Séance 7", "perso": "La Boîte de Jumanji", "outil": "Vidnoz", "classe": "boite",
    "titre": "Les illustrations — Texte et image",
    "texte": "[son de jungle, grondement lointain] Je suis Jumanji. Vous pensiez que l'aventure était terminée ? Elle ne l'est jamais vraiment. Aujourd'hui, je veux attirer votre attention sur quelque chose que vous avez peut-être oublié de regarder… vraiment regarder. Les images. Chris Van Allsburg n'est pas seulement l'auteur de cette histoire. Il en est aussi l'illustrateur. Chaque ombre, chaque angle, chaque regard… il les a choisis."
  },
  {
    "num": "Séance 8", "perso": "La Boîte de Jumanji", "outil": "Vidnoz", "classe": "boite",
    "titre": "Évaluation finale",
    "texte": "[son de jungle, lointain] Je suis Jumanji. Vous avez fait un long chemin. Vous avez suivi Judy et Peter. Maintenant… il est temps de voir ce que vous avez vraiment retenu. Ne craignez pas cette évaluation. C'est simplement le dernier jet de dés. Et n'oubliez pas… Jumanji attend toujours le prochain joueur. [grondement lointain qui s'éteint]"
  }
]

TYPE_LABELS = {"flash": "Dictée Flash", "trous": "Dictée à Trous", "coeur": "Par Cœur", "neg": "Négociée"}
TYPE_CLASSES = {"flash": "tb-flash", "trous": "tb-trous", "coeur": "tb-coeur", "neg": "tb-neg"}

def seance_cards():
    html = ""
    for s in SEANCES:
        has_video = "🎬" if s["video"] else ""
        video_badge = f'<div class="card-video-badge">🎬 Vidéo</div>' if s["video"] else ""
        html += f"""
    <div class="seance-card {s['personnage']}" onclick="openSeance({s['id']})">
      {video_badge}
      <div class="card-num">Séance {s['id']}</div>
      <span class="card-emoji">{s['emoji']}</span>
      <div class="card-titre">{s['titre']}</div>
      <div class="card-sous">{s['sous_titre']}</div>
      <div class="card-perso {s['personnage']}">
        {'👧 Judy' if s['personnage']=='judy' else ('👦 Peter' if s['personnage']=='peter' else '📦 La Boîte')}
      </div>
    </div>"""
    return html

def dictee_cards():
    html = ""
    for d in DICTEES:
        html += f"""
    <div class="dictee-card">
      <div class="dictee-type-badge {TYPE_CLASSES[d['type']]}">{TYPE_LABELS[d['type']]}</div>
      <div class="dictee-num">{d['num']} — {d['titre']}</div>
      <div class="dictee-sous">{d['sem']}</div>
      <div class="dictee-sous" style="margin-top:4px;font-size:0.74rem;">📌 {d['notions']}</div>
      <div class="dictee-links">
        <a class="dictee-link-btn dlb-eleve" href="Sequence_Dictees_Jumanji_CM2.html" target="_blank">📄 Fiche élève</a>
        <a class="dictee-link-btn dlb-prof" href="Fiche_Prof_Textes_Dictees_Jumanji.html" target="_blank">👩‍🏫 Fiche prof</a>
      </div>
    </div>"""
    return html

def script_blocks():
    html = ""
    for s in SCRIPTS:
        html += f"""
    <div class="script-block">
      <div class="script-block-header" onclick="toggleScript(this)">
        <div>
          <span class="script-block-num">{s['num']}</span>
          <span class="script-block-titre"> — {s['titre']}</span>
        </div>
        <span style="color:var(--text3);font-size:0.8rem;">
          <span class="card-perso {s['classe']}" style="padding:2px 8px;">{s['perso']} · {s['outil']}</span>
          &nbsp;▼
        </span>
      </div>
      <div class="script-block-body">{s['texte']}</div>
    </div>"""
    return html

# Build the full HTML
HTML = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Jumanji — Séquence CM2 · Lecture Suivie</title>
<style>
{CSS}
</style>
</head>
<body>

<!-- ════ SIDEBAR ════ -->
<nav class="sidebar">
  <div class="sidebar-logo" onclick="navigate('home')">
    <div class="logo-title">🌿 JUMANJI</div>
    <div class="logo-sub">Séquence CM2 · P5</div>
  </div>

  <div class="nav-section">Navigation</div>
  <div class="nav-item active" id="nav-home" onclick="navigate('home')">
    <span class="nav-emoji">🏠</span><span>Accueil</span>
  </div>
  <div class="nav-item" id="nav-seances" onclick="navigate('seances')">
    <span class="nav-emoji">📚</span><span>Séances</span>
  </div>
  <div class="nav-item" id="nav-dictees" onclick="navigate('dictees')">
    <span class="nav-emoji">✏️</span><span>Dictées</span>
  </div>
  <div class="nav-item" id="nav-grammaire" onclick="navigate('grammaire')">
    <span class="nav-emoji">🎮</span><span>Jeu Grammaire</span>
  </div>

  <div class="nav-divider"></div>
  <div class="nav-section">Espace</div>
  <div class="nav-item" id="nav-enseignant" onclick="navigate('enseignant')">
    <span class="nav-emoji">👩‍🏫</span><span>Enseignant</span>
  </div>
</nav>

<!-- ════ MAIN ════ -->
<main id="main">

  <!-- HOME -->
  <div class="view active" id="view-home">
    <div class="hero">
      <div class="hero-badge">Lecture suivie · CM2 · Période 5 · 2025-2026</div>
      <h1>JUMANJI</h1>
      <div class="hero-sub">Chris Van Allsburg</div>
      <div class="hero-desc">Une séquence complète de lecture suivie en 8 séances — avec vidéos, exercices interactifs, dictées et espace enseignant.</div>
    </div>

    <div class="home-grid">
      <div class="home-grid-title">📚 Les 8 séances — cliquez pour accéder à la vidéo + les exercices</div>
      <div class="seances-grid">
        {seance_cards()}
      </div>

      <div class="home-grid-title" style="margin-top: 8px;">⚡ Accès rapide</div>
      <div class="quick-access">
        <div class="qa-btn" onclick="navigate('dictees')">✏️ Séquence de dictées (10 dictées)</div>
        <div class="qa-btn" onclick="navigate('grammaire')">🎮 Jeu Pronoms de reprise</div>
        <div class="qa-btn" onclick="navigate('enseignant')">👩‍🏫 Espace enseignant</div>
      </div>
    </div>
  </div>

  <!-- SÉANCES LIST (redirection vers home) -->
  <div class="view" id="view-seances">
    <div class="hero" style="min-height:180px;padding:40px;">
      <div class="hero-badge">Toutes les séances</div>
      <h1 style="font-size:2rem">📚 Séances</h1>
    </div>
    <div class="home-grid">
      <div class="home-grid-title">Sélectionnez une séance pour accéder à la vidéo et aux exercices</div>
      <div class="seances-grid">
        {seance_cards()}
      </div>
    </div>
  </div>

  <!-- SEANCE VIEWS (generated dynamically) -->
  <div id="seance-views-container"></div>

  <!-- DICTÉES -->
  <div class="view" id="view-dictees">
    <div class="page-header-bar">
      <h2>✏️ Séquence de Dictées</h2>
      <p>10 dictées réparties sur 4 semaines · 4 types alternés · Liées aux séances de grammaire</p>
    </div>
    <div style="padding: 0 32px 12px;">
      <div style="display:flex;gap:10px;flex-wrap:wrap;">
        <span class="dictee-type-badge tb-flash" style="font-size:0.75rem;padding:4px 12px;">✏️ Dictée Flash — 10 min</span>
        <span class="dictee-type-badge tb-trous" style="font-size:0.75rem;padding:4px 12px;">📄 À Trous — 12-15 min</span>
        <span class="dictee-type-badge tb-coeur" style="font-size:0.75rem;padding:4px 12px;">🧠 Par Cœur — 10-15 min</span>
        <span class="dictee-type-badge tb-neg" style="font-size:0.75rem;padding:4px 12px;">🤝 Négociée — 15 min</span>
      </div>
    </div>
    <div class="dictees-grid">
      {dictee_cards()}
    </div>
    <div style="padding:0 32px 32px;">
      <div style="background:var(--card);border:1px solid var(--border);border-radius:12px;padding:20px;">
        <div class="ens-section-title" style="margin-bottom:12px;">📋 Tous les documents en un clic</div>
        <div style="display:flex;gap:10px;flex-wrap:wrap;">
          <a class="dictee-link-btn dlb-eleve" href="Sequence_Dictees_Jumanji_CM2.html" target="_blank" style="font-size:0.82rem;padding:8px 16px;">📄 Fiches élèves (10 dictées)</a>
          <a class="dictee-link-btn dlb-prof" href="Fiche_Prof_Textes_Dictees_Jumanji.html" target="_blank" style="font-size:0.82rem;padding:8px 16px;">👩‍🏫 Fiche prof — textes &amp; corrigés</a>
        </div>
      </div>
    </div>
  </div>

  <!-- GRAMMAIRE -->
  <div class="view" id="view-grammaire">
    <div class="grammaire-iframe-wrap">
      <iframe class="grammaire-iframe" src="PronomsReprise_Jeu_Jumanji.html" title="Jeu Pronoms de Reprise Jumanji"></iframe>
    </div>
  </div>

  <!-- ENSEIGNANT -->
  <div class="view" id="view-enseignant">
    <div class="page-header-bar">
      <h2>👩‍🏫 Espace Enseignant</h2>
      <p>Scripts des vidéos · Fiches séquence · Documents professeur</p>
    </div>
    <div class="enseignant-content">

      <div class="ens-section">
        <div class="ens-section-title">📂 Documents professeur</div>
        <div class="ens-cards">
          <a class="ens-card" href="Sequence_Dictees_Jumanji_CM2.html" target="_blank">
            <div class="ens-card-icon">📋</div>
            <div class="ens-card-title">Fiches séquence dictées</div>
            <div class="ens-card-desc">10 dictées élèves · 4 types · Programmation semaine par semaine</div>
          </a>
          <a class="ens-card" href="Fiche_Prof_Textes_Dictees_Jumanji.html" target="_blank">
            <div class="ens-card-icon">✅</div>
            <div class="ens-card-title">Fiche prof — Textes &amp; corrigés</div>
            <div class="ens-card-desc">Tous les textes à dicter + réponses attendues + conseils de lecture</div>
          </a>
          <a class="ens-card" href="PronomsReprise_Jeu_Jumanji.html" target="_blank">
            <div class="ens-card-icon">🎮</div>
            <div class="ens-card-title">Jeu Pronoms de reprise</div>
            <div class="ens-card-desc">Application interactive — Élimination + Texte à trous · Projetable en classe</div>
          </a>
          <div class="ens-card" onclick="navigate('dictees')">
            <div class="ens-card-icon">✏️</div>
            <div class="ens-card-title">Séquence de dictées</div>
            <div class="ens-card-desc">Accéder à toutes les dictées avec liens rapides</div>
          </div>
        </div>
      </div>

      <div class="ens-section">
        <div class="ens-section-title">🎬 Scripts des vidéos IA — 8 séances · 3 personnages</div>
        <div style="background:var(--card);border:1px solid var(--border);border-radius:10px;padding:14px 16px;margin-bottom:14px;">
          <div style="font-size:0.82rem;color:var(--text2);line-height:1.7;">
            <strong style="color:var(--gold)">3 personnages</strong> ·
            <span class="card-perso judy" style="padding:2px 8px;margin-right:4px;">👧 Judy — HeyGen · Séances 1, 2, 6</span>
            <span class="card-perso peter" style="padding:2px 8px;margin-right:4px;">👦 Peter — D-ID · Séances 3, 4, 5</span>
            <span class="card-perso boite" style="padding:2px 8px;">📦 La Boîte — Vidnoz · Séances 7, 8</span>
          </div>
        </div>
        {script_blocks()}
      </div>

      <div class="ens-section">
        <div class="ens-section-title">🗓️ Programmation de la séquence</div>
        <div style="background:var(--card);border:1px solid var(--border);border-radius:10px;padding:16px;">
          <table style="width:100%;border-collapse:collapse;font-size:0.82rem;">
            <thead>
              <tr>
                <th style="text-align:left;padding:6px 10px;color:var(--gold);font-size:0.72rem;text-transform:uppercase;letter-spacing:1px;border-bottom:1px solid var(--border);">Séance</th>
                <th style="text-align:left;padding:6px 10px;color:var(--gold);font-size:0.72rem;text-transform:uppercase;letter-spacing:1px;border-bottom:1px solid var(--border);">Activité</th>
                <th style="text-align:left;padding:6px 10px;color:var(--gold);font-size:0.72rem;text-transform:uppercase;letter-spacing:1px;border-bottom:1px solid var(--border);">Personnage</th>
                <th style="text-align:left;padding:6px 10px;color:var(--gold);font-size:0.72rem;text-transform:uppercase;letter-spacing:1px;border-bottom:1px solid var(--border);">Lien dictée</th>
              </tr>
            </thead>
            <tbody>
              <tr><td style="padding:7px 10px;border-bottom:1px solid var(--border);color:var(--text2);">1</td><td style="padding:7px 10px;border-bottom:1px solid var(--border);color:var(--text);">Découverte — couverture &amp; hypothèses</td><td style="padding:7px 10px;border-bottom:1px solid var(--border);"><span class="card-perso judy" style="padding:2px 7px;font-size:0.7rem;">Judy</span></td><td style="padding:7px 10px;border-bottom:1px solid var(--border);color:var(--text3);">J·1 Flash</td></tr>
              <tr><td style="padding:7px 10px;border-bottom:1px solid var(--border);color:var(--text2);">2</td><td style="padding:7px 10px;border-bottom:1px solid var(--border);color:var(--text);">Questionnaire 1 — situation initiale</td><td style="padding:7px 10px;border-bottom:1px solid var(--border);"><span class="card-perso judy" style="padding:2px 7px;font-size:0.7rem;">Judy</span></td><td style="padding:7px 10px;border-bottom:1px solid var(--border);color:var(--text3);">J·2 À Trous</td></tr>
              <tr><td style="padding:7px 10px;border-bottom:1px solid var(--border);color:var(--text2);">3</td><td style="padding:7px 10px;border-bottom:1px solid var(--border);color:var(--text);">Causes &amp; Effets — premiers dangers</td><td style="padding:7px 10px;border-bottom:1px solid var(--border);"><span class="card-perso peter" style="padding:2px 7px;font-size:0.7rem;">Peter</span></td><td style="padding:7px 10px;border-bottom:1px solid var(--border);color:var(--text3);">J·3 Flash + J·4 Trous</td></tr>
              <tr><td style="padding:7px 10px;border-bottom:1px solid var(--border);color:var(--text2);">4</td><td style="padding:7px 10px;border-bottom:1px solid var(--border);color:var(--text);">Frise chronologique — ordre des événements</td><td style="padding:7px 10px;border-bottom:1px solid var(--border);"><span class="card-perso peter" style="padding:2px 7px;font-size:0.7rem;">Peter</span></td><td style="padding:7px 10px;border-bottom:1px solid var(--border);color:var(--text3);">J·5 Négociée</td></tr>
              <tr><td style="padding:7px 10px;border-bottom:1px solid var(--border);color:var(--text2);">5</td><td style="padding:7px 10px;border-bottom:1px solid var(--border);color:var(--text);">Schéma narratif — la fin de l'aventure</td><td style="padding:7px 10px;border-bottom:1px solid var(--border);"><span class="card-perso peter" style="padding:2px 7px;font-size:0.7rem;">Peter</span></td><td style="padding:7px 10px;border-bottom:1px solid var(--border);color:var(--text3);">J·6 Par Cœur</td></tr>
              <tr><td style="padding:7px 10px;border-bottom:1px solid var(--border);color:var(--text2);">6</td><td style="padding:7px 10px;border-bottom:1px solid var(--border);color:var(--text);">Débat interprétatif</td><td style="padding:7px 10px;border-bottom:1px solid var(--border);"><span class="card-perso judy" style="padding:2px 7px;font-size:0.7rem;">Judy</span></td><td style="padding:7px 10px;border-bottom:1px solid var(--border);color:var(--text3);">J·7 À Trous</td></tr>
              <tr><td style="padding:7px 10px;border-bottom:1px solid var(--border);color:var(--text2);">7</td><td style="padding:7px 10px;border-bottom:1px solid var(--border);color:var(--text);">Illustrations — texte et image</td><td style="padding:7px 10px;border-bottom:1px solid var(--border);"><span class="card-perso boite" style="padding:2px 7px;font-size:0.7rem;">La Boîte</span></td><td style="padding:7px 10px;border-bottom:1px solid var(--border);color:var(--text3);">J·8 Par Cœur</td></tr>
              <tr><td style="padding:7px 10px;color:var(--text2);">8</td><td style="padding:7px 10px;color:var(--text);">Évaluation finale</td><td style="padding:7px 10px;"><span class="card-perso boite" style="padding:2px 7px;font-size:0.7rem;">La Boîte</span></td><td style="padding:7px 10px;color:var(--text3);">J·9 Flash + J·10 Négociée</td></tr>
            </tbody>
          </table>
        </div>
      </div>

    </div>
  </div>

</main>

<script>
/* ═══════════════════════════════════════════
   DATA
═══════════════════════════════════════════ */
const SEANCES_DATA = {json.dumps(SEANCES, ensure_ascii=False)};

/* ═══════════════════════════════════════════
   NAVIGATION
═══════════════════════════════════════════ */
let currentView = 'home';

function navigate(view) {{
  // Hide all views
  document.querySelectorAll('.view').forEach(v => v.classList.remove('active'));
  document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));

  const el = document.getElementById('view-' + view);
  if (el) {{
    el.classList.add('active');
    currentView = view;
    const navEl = document.getElementById('nav-' + view);
    if (navEl) navEl.classList.add('active');
  }}
  window.scrollTo(0, 0);
}}

function openSeance(id) {{
  const viewId = 'view-seance-' + id;
  let el = document.getElementById(viewId);
  if (!el) {{
    el = buildSeanceView(id);
    document.getElementById('seance-views-container').appendChild(el);
  }}
  document.querySelectorAll('.view').forEach(v => v.classList.remove('active'));
  document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));
  el.classList.add('active');
  document.getElementById('nav-seances').classList.add('active');
  currentView = 'seance-' + id;
  window.scrollTo(0, 0);
}}

/* ═══════════════════════════════════════════
   BUILD SEANCE VIEW
═══════════════════════════════════════════ */
function buildSeanceView(id) {{
  const s = SEANCES_DATA.find(x => x.id === id);
  if (!s) return document.createElement('div');

  const div = document.createElement('div');
  div.className = 'view active';
  div.id = 'view-seance-' + id;

  const persoLabel = s.personnage === 'judy' ? '👧 Judy' : (s.personnage === 'peter' ? '👦 Peter' : '📦 La Boîte');

  // Video section
  let videoHTML = '';
  if (s.video) {{
    videoHTML = `
      <div class="video-section">
        <div class="video-section-header">
          <span class="vh-badge">▶ Vidéo · Avant d'commencer</span>
          <span class="vh-title">Regardez la vidéo avant de faire les exercices</span>
        </div>
        <video class="video-player" controls preload="metadata" src="${{encodeURIPathSafe(s.video)}}">
          Votre navigateur ne supporte pas la lecture vidéo.
        </video>
        <div class="video-script">
          <div class="video-script-toggle" onclick="toggleScript(this)">
            <span>📜 Voir le script de la vidéo</span>
            <span>▼</span>
          </div>
          <div class="video-script-content">${{s.script}}</div>
        </div>
      </div>`;
  }} else {{
    videoHTML = `
      <div class="video-section">
        <div class="video-section-header">
          <span class="vh-badge">📜 Script</span>
          <span class="vh-title">Vidéo en préparation — Script disponible</span>
        </div>
        <div class="video-placeholder">
          <div class="vp-icon">🎬</div>
          <div class="vp-text" style="margin-bottom:10px;">Vidéo en préparation</div>
        </div>
        <div class="video-script">
          <div class="video-script-toggle open-default" onclick="toggleScript(this)">
            <span>📜 Script — ${{persoLabel}}</span>
            <span>▲</span>
          </div>
          <div class="video-script-content open">${{s.script}}</div>
        </div>
      </div>`;
  }}

  // Exercises
  let exercisesHTML = '';
  s.exercises.forEach((ex, i) => {{
    exercisesHTML += buildExercise(ex, `s${{id}}-ex${{i}}`);
  }});

  const objectifsHTML = s.objectifs.map(o => `<div class="objectif-item">${{o}}</div>`).join('');

  div.innerHTML = `
    <div class="seance-page">
      <div class="seance-back" onclick="navigate('seances')">← Retour aux séances</div>

      <div class="seance-header">
        <div class="seance-header-top">
          <div>
            <div class="seance-num-badge">Séance ${{id}} sur 8</div>
            <div class="seance-titre-main">${{s.emoji}} ${{s.titre}}</div>
            <div class="seance-sous-titre">${{s.sous_titre}}</div>
          </div>
          <div class="card-perso ${{s.personnage}}" style="flex-shrink:0;">${{persoLabel}}</div>
        </div>
        <div class="objectifs-list">
          <div style="font-size:0.72rem;text-transform:uppercase;letter-spacing:1px;color:var(--text3);margin-bottom:4px;">Objectifs de la séance</div>
          ${{objectifsHTML}}
        </div>
      </div>

      ${{videoHTML}}

      <div style="font-size:0.75rem;text-transform:uppercase;letter-spacing:2px;color:var(--text3);margin-bottom:14px;">Exercices</div>
      <div class="exercises-section">
        ${{exercisesHTML}}
      </div>
    </div>`;

  // Init exercises after render
  setTimeout(() => {{
    s.exercises.forEach((ex, i) => {{
      initExercise(ex, `s${{id}}-ex${{i}}`, div);
    }});
  }}, 50);

  return div;
}}

function encodeURIPathSafe(path) {{
  return path.split('/').map(p => encodeURIComponent(p)).join('/');
}}

/* ═══════════════════════════════════════════
   BUILD EXERCISE HTML
═══════════════════════════════════════════ */
function buildExercise(ex, uid) {{
  let typeLabel, typeClass, body;

  if (ex.type === 'relier') {{
    typeLabel = '🔗 Exercice de liaison'; typeClass = 'badge-relier';
    body = buildRelierHTML(ex, uid);
  }} else if (ex.type === 'qcm') {{
    typeLabel = '🔘 QCM'; typeClass = 'badge-qcm';
    body = buildQCMHTML(ex, uid);
  }} else if (ex.type === 'vf') {{
    typeLabel = '✓✗ Vrai ou Faux'; typeClass = 'badge-vf';
    body = buildVFHTML(ex, uid);
  }} else if (ex.type === 'ordre') {{
    typeLabel = '🔢 Ordre chronologique'; typeClass = 'badge-ordre';
    body = buildOrdreHTML(ex, uid);
  }} else {{
    body = '';
  }}

  return `
    <div class="exercise-card">
      <div class="exercise-card-header">
        <span class="exercise-type-badge ${{typeClass}}">${{typeLabel}}</span>
        <span class="exercise-title">${{ex.titre}}</span>
      </div>
      <div class="exercise-body">
        ${{ex.consigne ? `<div class="exercise-consigne">${{ex.consigne}}</div>` : ''}}
        ${{body}}
      </div>
    </div>`;
}}

/* ─── RELIER HTML ─── */
function buildRelierHTML(ex, uid) {{
  // Right items will be shuffled by initExercise
  const leftItems = ex.pairs.map((p, i) =>
    `<div class="relier-item" data-pid="${{i}}" data-side="left">${{p.left}}</div>`
  ).join('');

  // Placeholder right items (will be replaced by initExercise)
  const rightItems = ex.pairs.map((p, i) =>
    `<div class="relier-item" data-pid="${{i}}" data-side="right" style="display:none">${{p.right}}</div>`
  ).join('');

  return `
    <div class="relier-wrap" id="relier-${{uid}}">
      <div class="relier-cols">
        <div class="relier-left-col">${{leftItems}}</div>
        <div class="relier-mid">
          <svg class="relier-svg" xmlns="http://www.w3.org/2000/svg" style="position:absolute;top:0;left:-40px;width:160px;overflow:visible;pointer-events:none;"></svg>
        </div>
        <div class="relier-right-col">${{rightItems}}</div>
      </div>
      <div class="relier-result"></div>
    </div>`;
}}

/* ─── QCM HTML ─── */
function buildQCMHTML(ex, uid) {{
  const letters = ['A', 'B', 'C', 'D', 'E'];
  const optHtml = ex.options.map((o, i) => {{
    const isDebate = ex.debate;
    const cls = isDebate ? 'qcm-option debate' : 'qcm-option';
    return `<div class="${{cls}}" data-correct="${{o.correct}}" data-index="${{i}}" id="opt-${{uid}}-${{i}}" onclick="handleQCM(this,'${{uid}}','${{isDebate}}')">
      <div class="opt-letter">${{letters[i]}}</div>
      <div>${{o.text}}</div>
    </div>`;
  }}).join('');

  return `
    <div id="qcm-${{uid}}">
      <div class="qcm-question">${{ex.question}}</div>
      <div class="qcm-options">${{optHtml}}</div>
      <div class="qcm-feedback" id="fb-${{uid}}">${{ex.feedback}}</div>
    </div>`;
}}

/* ─── VF HTML ─── */
function buildVFHTML(ex, uid) {{
  const itemsHtml = ex.items.map((item, i) => `
    <div class="vf-item" id="vfi-${{uid}}-${{i}}">
      <div class="vf-statement">
        <span class="vf-num">${{i+1}}.</span>
        <span>${{item.s}}</span>
      </div>
      <div class="vf-buttons">
        <div class="vf-btn vf-btn-v" onclick="handleVF(this,'${{uid}}',${{i}},true,${{item.ok}})">✓ VRAI</div>
        <div class="vf-btn vf-btn-f" onclick="handleVF(this,'${{uid}}',${{i}},false,${{item.ok}})">✗ FAUX</div>
      </div>
      <div class="vf-explication" id="vfexp-${{uid}}-${{i}}">${{item.exp}}</div>
    </div>`).join('');

  return `<div class="vf-list" id="vf-${{uid}}">${{itemsHtml}}</div>`;
}}

/* ─── ORDRE HTML ─── */
function buildOrdreHTML(ex, uid) {{
  // Shuffle items initially
  const shuffled = [...ex.items].sort(() => Math.random() - 0.5);
  const itemsHtml = shuffled.map((item, i) => `
    <div class="ordre-item" data-correct="${{item.pos}}" id="ord-${{uid}}-${{i}}">
      <span class="ordre-item-emoji">${{item.emoji}}</span>
      <span class="ordre-item-text">${{item.text}}</span>
      <div class="ordre-moves">
        <button class="ordre-btn" onclick="moveOrdre('${{uid}}',${{i}},-1)" ${{i===0?'disabled':''}}>↑</button>
        <button class="ordre-btn" onclick="moveOrdre('${{uid}}',${{i}},1)" ${{i===shuffled.length-1?'disabled':''}}>↓</button>
      </div>
    </div>`).join('');

  return `
    <div>
      <div class="ordre-list" id="ordre-list-${{uid}}">${{itemsHtml}}</div>
      <div class="ordre-check">
        <button class="btn-check" onclick="checkOrdre('${{uid}}',${{ex.items.length}})">Vérifier l'ordre</button>
        <div class="ordre-result" id="ordre-result-${{uid}}"></div>
      </div>
    </div>`;
}}

function escapeStr(s) {{
  return s.replace(/'/g, "\\'").replace(/"/g, '&quot;');
}}

/* ═══════════════════════════════════════════
   INIT EXERCISES
═══════════════════════════════════════════ */
function initExercise(ex, uid, container) {{
  if (ex.type === 'relier') {{
    initRelier(uid, ex.pairs);
  }}
}}

/* ═══════════════════════════════════════════
   RELIER ENGINE
═══════════════════════════════════════════ */
function initRelier(uid, pairs) {{
  const wrap = document.getElementById('relier-' + uid);
  if (!wrap) return;

  const leftCol = wrap.querySelector('.relier-left-col');
  const rightCol = wrap.querySelector('.relier-right-col');
  const svg = wrap.querySelector('.relier-svg');

  // Shuffle pairs for right column
  const indices = pairs.map((_, i) => i);
  for (let i = indices.length - 1; i > 0; i--) {{
    const j = Math.floor(Math.random() * (i + 1));
    [indices[i], indices[j]] = [indices[j], indices[i]];
  }}

  // Clear and rebuild right column with shuffled order
  rightCol.innerHTML = '';
  indices.forEach(origIdx => {{
    const el = document.createElement('div');
    el.className = 'relier-item';
    el.dataset.pid = origIdx;
    el.dataset.side = 'right';
    el.textContent = pairs[origIdx].right;
    rightCol.appendChild(el);
  }});

  // State
  let selectedLeft = null;
  let correctCount = 0;

  // Resize SVG to cover the wrap
  function resizeSVG() {{
    const h = wrap.querySelector('.relier-cols').offsetHeight;
    svg.style.height = h + 'px';
    svg.setAttribute('height', h);
  }}
  setTimeout(resizeSVG, 100);

  // Left items handler
  leftCol.querySelectorAll('.relier-item').forEach(el => {{
    el.addEventListener('click', () => {{
      if (el.classList.contains('matched-ok')) return;
      leftCol.querySelectorAll('.relier-item').forEach(e => e.classList.remove('selected'));
      el.classList.add('selected');
      selectedLeft = el;
    }});
  }});

  // Right items handler
  rightCol.querySelectorAll('.relier-item').forEach(el => {{
    el.addEventListener('click', () => {{
      if (!selectedLeft || el.classList.contains('matched-ok')) return;

      const leftPid = parseInt(selectedLeft.dataset.pid);
      const rightPid = parseInt(el.dataset.pid);

      if (leftPid === rightPid) {{
        // ✅ Correct!
        selectedLeft.classList.remove('selected');
        selectedLeft.classList.add('matched-ok');
        el.classList.add('matched-ok');
        drawReliefLine(wrap, svg, selectedLeft, el);
        correctCount++;
        selectedLeft = null;

        if (correctCount === pairs.length) {{
          wrap.querySelector('.relier-result').textContent = '✅ Excellent ! Toutes les liaisons sont correctes !';
        }}
      }} else {{
        // ❌ Wrong
        selectedLeft.classList.add('shake');
        el.classList.add('shake');
        setTimeout(() => {{
          if (selectedLeft) selectedLeft.classList.remove('shake', 'selected');
          el.classList.remove('shake');
          selectedLeft = null;
        }}, 500);
      }}
    }});
  }});
}}

function drawReliefLine(wrap, svg, fromEl, toEl) {{
  resizeSVGToWrap(wrap, svg);

  const wrapRect = wrap.getBoundingClientRect();
  const fromRect = fromEl.getBoundingClientRect();
  const toRect = toEl.getBoundingClientRect();

  const x1 = fromRect.right - wrapRect.left;
  const y1 = fromRect.top + fromRect.height / 2 - wrapRect.top;
  const x2 = toRect.left - wrapRect.left;
  const y2 = toRect.top + toRect.height / 2 - wrapRect.top;

  // Bezier control points
  const cx1 = x1 + (x2 - x1) * 0.35;
  const cx2 = x1 + (x2 - x1) * 0.65;

  const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
  path.setAttribute('d', `M${{x1}},${{y1}} C${{cx1}},${{y1}} ${{cx2}},${{y2}} ${{x2}},${{y2}}`);
  path.setAttribute('stroke', '#4ade80');
  path.setAttribute('stroke-width', '2.5');
  path.setAttribute('fill', 'none');
  path.setAttribute('stroke-linecap', 'round');
  path.style.filter = 'drop-shadow(0 0 3px rgba(74,222,128,0.6))';

  // Animate
  const len = path.getTotalLength ? path.getTotalLength() : 200;
  path.style.strokeDasharray = len;
  path.style.strokeDashoffset = len;
  path.style.transition = 'stroke-dashoffset 0.4s ease';
  svg.appendChild(path);
  requestAnimationFrame(() => {{
    requestAnimationFrame(() => {{
      path.style.strokeDashoffset = 0;
    }});
  }});
}}

function resizeSVGToWrap(wrap, svg) {{
  const cols = wrap.querySelector('.relier-cols');
  const h = cols ? cols.offsetHeight + 20 : 400;
  const w = wrap.offsetWidth;
  svg.style.width = w + 'px';
  svg.style.height = h + 'px';
  svg.style.top = '0';
  svg.style.left = '0';
  svg.style.position = 'absolute';
}}

/* ═══════════════════════════════════════════
   QCM ENGINE
═══════════════════════════════════════════ */
function handleQCM(optEl, uid, isDebate) {{
  const container = document.getElementById('qcm-' + uid);
  const fb = document.getElementById('fb-' + uid);

  if (isDebate === 'true') {{
    // Debate mode: just highlight selection
    container.querySelectorAll('.qcm-option').forEach(o => o.classList.remove('debate-selected'));
    optEl.classList.add('debate-selected');
    fb.classList.add('visible');
    return;
  }}

  // Check if already answered
  if (container.dataset.answered) return;

  const isCorrect = optEl.dataset.correct === 'true';

  if (isCorrect) {{
    optEl.classList.add('correct');
    fb.classList.add('visible');
    container.dataset.answered = '1';
    // Disable all options
    container.querySelectorAll('.qcm-option').forEach(o => o.style.cursor = 'default');
  }} else {{
    optEl.classList.add('wrong');
    setTimeout(() => optEl.classList.remove('wrong'), 1000);
  }}
}}

/* ═══════════════════════════════════════════
   VRAI/FAUX ENGINE
═══════════════════════════════════════════ */
function handleVF(btnEl, uid, idx, userAnswer, correct, expl) {{
  const item = document.getElementById('vfi-' + uid + '-' + idx);
  const expEl = document.getElementById('vfexp-' + uid + '-' + idx);

  if (item.dataset.answered) return;
  item.dataset.answered = '1';

  const isCorrect = userAnswer === correct;
  expEl.classList.add('visible');

  if (isCorrect) {{
    btnEl.classList.add('active-ok');
    item.classList.add('correct');
  }} else {{
    btnEl.classList.add('active-wrong');
    item.classList.add('wrong-ans');
    // Show the correct button
    const buttons = item.querySelectorAll('.vf-btn');
    buttons.forEach(b => {{
      const bIsTrue = b.classList.contains('vf-btn-v');
      if (bIsTrue === correct) b.classList.add('active-ok');
    }});
  }}
}}

/* ═══════════════════════════════════════════
   ORDRE ENGINE
═══════════════════════════════════════════ */
function moveOrdre(uid, idx, dir) {{
  const list = document.getElementById('ordre-list-' + uid);
  const items = Array.from(list.querySelectorAll('.ordre-item'));
  const newIdx = idx + dir;
  if (newIdx < 0 || newIdx >= items.length) return;

  const a = items[idx];
  const b = items[newIdx];

  if (dir === 1) {{
    list.insertBefore(b, a);
  }} else {{
    list.insertBefore(a, b);
  }}

  // Rebuild buttons
  const newItems = Array.from(list.querySelectorAll('.ordre-item'));
  newItems.forEach((el, i) => {{
    const btns = el.querySelectorAll('.ordre-btn');
    btns[0].disabled = i === 0;
    btns[1].disabled = i === newItems.length - 1;
    btns[0].setAttribute('onclick', `moveOrdre('${{uid}}',${{i}},-1)`);
    btns[1].setAttribute('onclick', `moveOrdre('${{uid}}',${{i}},1)`);
  }});
}}

function checkOrdre(uid, total) {{
  const list = document.getElementById('ordre-list-' + uid);
  const items = Array.from(list.querySelectorAll('.ordre-item'));
  const correctPositions = items.map(el => parseFloat(el.dataset.correct));
  const sorted = [...correctPositions].sort((a, b) => a - b);
  let correct = 0;
  items.forEach((el, i) => {{
    const expectedPos = sorted[i];
    if (parseFloat(el.dataset.correct) === expectedPos) {{
      el.classList.add('correct-pos');
      correct++;
    }} else {{
      el.classList.remove('correct-pos');
    }}
  }});
  const result = document.getElementById('ordre-result-' + uid);
  if (correct === total) {{
    result.textContent = '✅ Parfait ! Tous les événements sont dans le bon ordre !';
    result.style.color = 'var(--green)';
  }} else {{
    result.textContent = `${{correct}}/${{total}} dans le bon ordre. Réessaie !`;
    result.style.color = 'var(--gold)';
  }}
}}

/* ═══════════════════════════════════════════
   TOGGLE HELPERS
═══════════════════════════════════════════ */
function toggleScript(headerEl) {{
  const content = headerEl.nextElementSibling;
  if (!content) return;
  content.classList.toggle('open');
  const arrow = headerEl.querySelector('span:last-child');
  if (arrow) arrow.textContent = content.classList.contains('open') ? '▲' : '▼';
}}

/* ═══════════════════════════════════════════
   INIT
═══════════════════════════════════════════ */
// Pre-build séance 1 for fast first load
window.addEventListener('DOMContentLoaded', () => {{
  navigate('home');
}});
</script>

</body>
</html>"""

output_path = "/sessions/determined-relaxed-planck/mnt/Projets/Pédagogie CM2/Français/Séquence sur Jumanji/index.html"
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(HTML)

print(f"✅ Site généré : {len(HTML)} caractères, ~{len(HTML.splitlines())} lignes")
print(f"📍 Fichier : {output_path}")
