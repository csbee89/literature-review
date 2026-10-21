// 문헌 선정 과정·정리 일정 설명 슬라이드(학생 모임용). 수치 출처: review/prisma_flow.md, review/*.csv, students/assignments.csv
// 사용: node scripts/make_selection_deck.js handover/선정과정_설명.pptx
const pptxgen = require("pptxgenjs");
const { applyTheme } = require("/root/.claude/skills/synced/36061253-cad3-474f-a958-6ae3e5d87192_6ef3f8a9-87be-4fc6-b633-da626a771d08/pptx/scripts/apply_theme.js");

const OUT = process.argv[2] || "handover/선정과정_설명.pptx";
const INK = "1F2933", ACC = "B0431F", GRAY = "8B95A1", LINE = "D5D9DE";
const THEME = {
  name: "Liquidity Review", headFontFace: "Noto Sans KR", bodyFontFace: "Noto Sans KR",
  colors: { dk1: INK, lt1: "FFFFFF", dk2: "3E4C59", lt2: "F5F7F9", accent1: ACC, accent2: GRAY, accent3: LINE,
            accent4: "52606D", accent5: "9AA5B1", accent6: "CBD2D9", hlink: ACC, folHlink: "7B8794" },
};

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE"; // 13.333 x 7.5 in
pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
pres.title = "문헌 선정 과정과 정리 일정";
const C = pres.SchemeColor;

pres.defineSlideMaster({
  title: "COVER", background: { color: "FFFFFF" },
  objects: [
    { line: { x: 0.8, y: 4.55, w: 11.73, h: 0, line: { color: LINE, width: 1 } } },
    { placeholder: { options: { name: "title", type: "title", x: 0.8, y: 2.3, w: 11.7, h: 1.6, fontSize: 40, bold: true, color: C.text1, valign: "bottom", align: "left", margin: 0 }, text: "" } },
    { placeholder: { options: { name: "body", type: "body", x: 0.8, y: 4.8, w: 11.7, h: 1.0, fontSize: 15, color: C.accent2, valign: "top", margin: 0 }, text: "" } },
  ],
});
pres.defineSlideMaster({
  title: "CONTENT", background: { color: "FFFFFF" },
  slideNumber: { x: 12.23, y: 7.02, w: 0.5, h: 0.3, fontSize: 10, color: GRAY, align: "right" },
  objects: [
    { text: { text: "주택시장 유동성 지표 리뷰", options: { x: 0.6, y: 0.18, w: 6, h: 0.3, fontSize: 10, color: GRAY, margin: 0 } } },
    { placeholder: { options: { name: "title", type: "title", x: 0.6, y: 0.5, w: 12.1, h: 0.62, fontSize: 26, bold: true, color: C.text1, valign: "middle", align: "left", margin: 0 }, text: "" } },
    { placeholder: { options: { name: "source", type: "body", x: 0.6, y: 7.02, w: 10.5, h: 0.3, fontSize: 10, color: C.accent2, valign: "middle", margin: 0 }, text: "" } },
  ],
});

const T = (s, str, o) => s.addText(str, Object.assign({ isTextBox: true, margin: 0, fontSize: 14, color: INK, valign: "middle" }, o));
const box = (s, x, y, w, h, name) => s.addShape(pres.shapes.RECTANGLE, { x, y, w, h, fill: { color: "FFFFFF" }, line: { color: INK, width: 1 }, objectName: name });
const arrow = (s, x1, y1, x2, y2, back) => s.addShape(pres.shapes.LINE, {
  x: Math.min(x1, x2), y: Math.min(y1, y2), w: Math.abs(x2 - x1), h: Math.abs(y2 - y1),
  line: Object.assign({ color: GRAY, width: 1 }, back ? { beginArrowType: "triangle" } : { endArrowType: "triangle" }) });

// 1. 표지
{
  const s = pres.addSlide({ masterName: "COVER" });
  s.addText("주택시장 유동성 지표 체계적 문헌고찰", { placeholder: "title" });
  s.addText([
    { text: "문헌 선정 과정과 정리 일정", options: { breakLine: true } },
    { text: "가천대학교 도시계획전공 연구실 · 2026.10.28 첫 모임", options: { fontSize: 13 } },
  ], { placeholder: "body" });
  s.addNotes("Journal of Housing Economics 투고를 목표로 하는 체계적 문헌고찰. 오늘은 148편이 어떻게 골라졌는지와 앞으로 12주 일정을 본다.");
}

// 2. PRISMA 흐름도
{
  const s = pres.addSlide({ masterName: "CONTENT" });
  s.addText("문헌 선정 흐름", { placeholder: "title" });
  s.addText("자료: 연구실 검색 기록(검색 2026-10-10, 원문 현황 2026-10-21). PRISMA 2020 형식", { placeholder: "source" });
  const MX = 1.65, MW = 4.95, RX = 7.2, RW = 5.5, top = 1.32, H = 0.78, G = 0.17;
  const y = (i) => top + i * (H + G);
  const main = [
    [["데이터베이스·학술지 검색 ", {}], ["52,006", { bold: true }], ["건", {}]],
    [["규칙 선별 대상 ", {}], ["37,104", { bold: true }], ["건", {}]],
    [["제목·초록 판독 ", {}], ["1,400", { bold: true }], ["건", {}]],
    [["제목·초록 통과 ", {}], ["438", { bold: true }], ["편", {}]],
    [["종합 대상 ", {}], ["148", { bold: true, color: ACC }], ["편", {}]],
    [["원문 확보(게재본) ", {}], ["137", { bold: true }], ["편", {}]],
  ];
  const mainSub = [
    "Semantic Scholar 4,351 · Crossref 16,800 · 핵심 학술지 16종 26,581 · 인용 추적 876 · OpenAlex 3,398",
    "", "", "", "C1 측정·정의·지수 56 · C2 선행성·정보내용 92", "학생 정리 W1~W11, 예시 2편 제외 146편 배정",
  ];
  main.forEach((runs, i) => {
    box(s, MX, y(i), MW, H, `main${i + 1}`);
    const r = runs.map(([t, o]) => ({ text: t, options: Object.assign({ fontSize: 15 }, o) }));
    if (mainSub[i]) { r[r.length - 1].options.breakLine = true; r.push({ text: mainSub[i], options: { fontSize: 11, color: GRAY } }); }
    T(s, r, { x: MX + 0.15, y: y(i) + 0.04, w: MW - 0.3, h: H - 0.08, objectName: `mainText${i + 1}` });
    if (i < main.length - 1) arrow(s, MX + MW / 2, y(i) + H, MX + MW / 2, y(i + 1));
  });
  const side = [
    [0, "중복 제거 ", "14,902", "건", "DOI·정규화 제목 기준, 게재본 우선"],
    [1, "규칙으로 제외 ", "35,704", "건", "주택 맥락어 없음 17,271 · 유동성 지표어 없음 12,185 · 강한 지표어 없음 2,847 · 노이즈 어휘 2,164 · OpenAlex 경로 1,151 · 과학 학술지 86"],
    [2, "판독으로 제외 ", "1,044", "건", "주제 밖 764 · 지표 측정 없음 93 · 문헌 유형 밖 79 · 시장 범위 밖 78 · 중복 28 · 선행 리뷰 2"],
    [3, "다른 경로로 추가 ", "82", "편", "핵심 앵커 문헌 21 · 복구 검색 51 · 게재본 확인 10"],
    [4, "종합 밖 ", "290", "편", "증거지도 253(지표가 결과변수) · 이론 배경 37"],
    [5, "원문 대기 ", "11", "편", "원문 없음 8 · 워킹페이퍼판만 3 → W12"],
  ];
  side.forEach(([i, a, n, u, sub]) => {
    box(s, RX, y(i), RW, H, `side${i + 1}`);
    T(s, [
      { text: a, options: { fontSize: 14 } }, { text: n, options: { fontSize: 14, bold: true } }, { text: u, options: { fontSize: 14, breakLine: true } },
      { text: sub, options: { fontSize: 11, color: GRAY } },
    ], { x: RX + 0.15, y: y(i) + 0.04, w: RW - 0.3, h: H - 0.08, objectName: `sideText${i + 1}` });
    arrow(s, MX + MW, y(i) + H / 2, RX, y(i) + H / 2, i === 3);
  });
  // 단계 라벨
  [["식별", 0, 0], ["선별", 1, 3], ["적격성", 4, 5]].forEach(([lab, a, b]) => {
    T(s, lab, { x: 0.6, y: y(a), w: 0.85, h: y(b) + H - y(a), fontSize: 13, color: GRAY, bold: true, valign: "middle" });
    s.addShape(pres.shapes.LINE, { x: 1.42, y: y(a), w: 0, h: y(b) + H - y(a), line: { color: LINE, width: 1 } });
  });
  s.addNotes([
    "왼쪽 줄이 본류, 오른쪽이 빠지거나 더해진 것.",
    "식별: 5개 경로로 52,006건. 핵심 학술지 16종(REE, JREFE, JHE, JUE, RSUE, JHR, JRER, Housing Studies, IJHMA, JPR, JREL, HPD, JHBE, Urban Studies, JERER, REMV)은 1986년 이후 전 논문을 받았다. 중복 14,902건을 지워 37,104건.",
    "규칙 선별: 제목·초록에 주택 맥락어와 유동성 지표어(TOM, DOM, 거래량, 호가 대비 거래가 등 강한 용어)가 함께 있어야 통과. 기계적 규칙이라 재현 가능하다. 35,704건 제외, 1,400건 남음.",
    "판독: 1,400건을 한 편씩 읽어 438편 통과. 제외 사유 코드 E1~E4(다음 장). 검색으로 안 잡힌 핵심 문헌(앵커, AER·JPE 등 일반 경제학지)과 복구 검색, 워킹페이퍼의 게재본 확인으로 82편을 더했다.",
    "적격성: 438편에 '지표가 연구의 대상인가' 기준을 적용해 148편. 나머지 253편은 증거지도(건수만 센다), 37편은 이론 배경.",
    "판독은 AI 보조(Claude) 1인 판정이라, 교수와 손수연이 무작위 140건·보류 47건·E2/E3 142건을 다시 판독해 일치도(kappa)를 보고한다.",
    "148편 중 137편은 게재본 원문 확보. 8편은 원문 없음, 3편은 워킹페이퍼판만 있어 W12로 미뤘다. 끝내 못 구하면 PRISMA에 '원문 확보 실패'로 적는다. 예시 2편(p115, p033)은 Claude가 정리해 배정에서 뺐다.",
  ].join("\n"));
}

// 3. 제외 사유 표
{
  const s = pres.addSlide({ masterName: "CONTENT" });
  s.addText("단계별 제외 사유", { placeholder: "title" });
  s.addText("자료: review/screening_all_records.csv, screening_read_set.csv, screening_openalex.csv", { placeholder: "source" });
  const hdr = (cells) => cells.map((t, j) => ({ text: t, options: { bold: true, align: j === cells.length - 1 ? "right" : "left", border: [{ pt: 2, color: INK }, { type: "none" }, { pt: 1, color: INK }, { type: "none" }] } }));
  const row = (cells, last) => cells.map((t, j) => ({ text: t, options: { align: j === cells.length - 1 ? "right" : "left", bold: !!last, border: [{ type: "none" }, { type: "none" }, last ? { pt: 1.5, color: INK } : { pt: 1, color: LINE }, { type: "none" }] } }));
  const opt = (x, w, colW) => ({ x, y: 1.95, w, colW, fontSize: 14, color: INK, rowH: 0.5, valign: "middle", margin: [0, 0.08, 0, 0.08] });
  T(s, [{ text: "규칙 선별", options: { bold: true } }, { text: "  37,104 → 1,400", options: { color: GRAY } }], { x: 0.6, y: 1.35, w: 5.6, h: 0.45, fontSize: 17 });
  s.addTable([
    hdr(["제외 규칙", "건수"]),
    row(["주택 맥락어 없음", "17,271"]), row(["유동성 지표어 없음", "12,185"]), row(["강한 지표어 없음(TOM·DOM·호가 변경 등)", "2,847"]),
    row(["노이즈 어휘(증권·재료과학 등)", "2,164"]), row(["OpenAlex 경로 규칙·학술지 제외", "1,151"]), row(["과학 학술지", "86"]),
    row(["합계", "35,704"], true),
  ], opt(0.6, 5.6, [4.3, 1.3]));
  T(s, [{ text: "제목·초록 판독", options: { bold: true } }, { text: "  1,400 → 356", options: { color: GRAY } }], { x: 6.9, y: 1.35, w: 5.8, h: 0.45, fontSize: 17 });
  s.addTable([
    hdr(["코드", "사유", "건수"]),
    row(["E1", "범위 밖 유동성·비주택 주제", "764"]), row(["E2", "유동성 지표 측정 없음", "93"]),
    row(["E4", "문헌 유형 밖(워킹페이퍼·학위논문·학술대회)", "79"]), row(["E3", "시장 범위 밖(임대·상업용·토지·분양)", "78"]),
    row(["", "중복", "28"]), row(["R", "선행 리뷰", "2"]),
    row(["", "합계", "1,044"], true),
  ], opt(6.9, 5.8, [0.7, 4.0, 1.1]));
  s.addNotes("규칙 선별은 정규식 규칙이라 누가 돌려도 같은 결과. 판독은 한 편씩 읽고 코드를 붙였다. E1이 가장 많은 것은 '유동성'이 증권·통화 유동성, 가계 유동성 제약 같은 다른 뜻으로도 쓰이기 때문. 판독 통과 356편에 다른 경로 82편을 더해 438편.");
}

// 4. 종합 대상 기준
{
  const s = pres.addSlide({ masterName: "CONTENT" });
  s.addText("종합 대상 기준", { placeholder: "title" });
  s.addText("자료: review/included_studies.csv(scope·criterion 열), 프로토콜 v0.7.3 §4.4. 연구책임자 승인 2026-10-11", { placeholder: "source" });
  T(s, [{ text: "438편 중 ", options: { color: GRAY } }, { text: "유동성 지표가 연구의 대상인 논문만", options: { bold: true } }], { x: 0.6, y: 1.35, w: 12.1, h: 0.5, fontSize: 20 });
  const cols = [
    { x: 0.6, n: "148", c: ACC, lab: "종합", lines: ["C1 측정·정의·지수 56", "C2 선행성·정보내용 92", "워드 1쪽 + 시트 추출"] },
    { x: 4.75, n: "253", c: INK, lab: "증거지도", lines: ["지표가 결과변수", "홍수·학군·정책 → TOM·거래량", "건수만 집계"] },
    { x: 8.9, n: "37", c: INK, lab: "배경", lines: ["탐색·매칭 이론 모형", "서론·개념 틀 인용", "추출 없음"] },
  ];
  cols.forEach((c, i) => {
    T(s, c.n, { x: c.x, y: 2.1, w: 3.6, h: 1.7, fontSize: 100, bold: true, color: c.c, valign: "bottom", objectName: `num${i}` });
    T(s, c.lab, { x: c.x, y: 3.95, w: 3.6, h: 0.55, fontSize: 22, bold: true });
    s.addShape(pres.shapes.LINE, { x: c.x, y: 4.65, w: 3.6, h: 0, line: { color: LINE, width: 1 } });
    T(s, c.lines.map((t, j) => ({ text: t, options: { breakLine: j < c.lines.length - 1 } })), { x: c.x, y: 4.85, w: 3.75, h: 1.9, fontSize: 17, valign: "top", paraSpaceAfter: 10 });
    if (i < 2) s.addShape(pres.shapes.LINE, { x: c.x + 3.95, y: 2.3, w: 0, h: 4.3, line: { color: LINE, width: 1 } });
  });
  s.addNotes([
    "가장 중요한 기준. 우리 리뷰의 질문은 '유동성을 어떻게 재고, 그 지표가 무엇을 알려 주는가'이다.",
    "C1: 매물 시간·거래량·호가 대비 거래가 같은 지표를 정의하거나, 측정 문제(절단·재등록·철회 매물)를 다루거나, 지수를 만든 논문.",
    "C2: 그 지표가 가격 등을 앞서는지, 정보를 담고 있는지 검정한 논문.",
    "증거지도 253편: 예를 들어 홍수 위험이 매물 시간을 늘리는가처럼 지표를 결과변수로만 쓴 연구. 버리는 게 아니라 연도·국가·지표별 건수 그림 1장으로 쓴다.",
    "배경 37편: 탐색·매칭 이론 모형. 서론과 개념 틀에서 인용한다.",
  ].join("\n"));
}

// 5. 148편 분류 매트릭스
{
  const s = pres.addSlide({ masterName: "CONTENT" });
  s.addText("종합 148편 분류", { placeholder: "title" });
  s.addText("자료: review/synthesis_set.csv. 초기 코드, 학생이 정리하며 확인·수정", { placeholder: "source" });
  const M = [["S1 수요·관심", 4, 0, 21], ["S2 공급·호가 설정", 7, 3, 6], ["S3 매칭(매물 시간)", 13, 17, 9], ["S4 체결(거래량·가격)", 6, 6, 40], ["S5 집계 상태·지수", 9, 0, 7]];
  const b = (top, bottom) => [top || { type: "none" }, { type: "none" }, bottom || { type: "none" }, { type: "none" }];
  const rows = [[
    { text: "거래 사슬 단계", options: { bold: true, border: b({ pt: 2, color: INK }, { pt: 1, color: INK }) } },
    ...["F1 정의·구축", "F2 측정 쟁점", "F3 선행·관계", "계"].map((t) => ({ text: t, options: { bold: true, fontSize: 14, align: "right", border: b({ pt: 2, color: INK }, { pt: 1, color: INK }) } })),
  ]];
  M.forEach(([lab, ...v]) => {
    const cells = [...v, v.reduce((a, c) => a + c, 0)];
    rows.push([{ text: lab, options: { border: b(null, { pt: 1, color: LINE }) } },
      ...cells.map((n, j) => ({ text: String(n), options: { align: "right", bold: j === 3, color: n === 40 ? ACC : INK, border: b(null, { pt: 1, color: LINE }) } }))]);
  });
  rows.push([{ text: "계", options: { bold: true, border: b(null, { pt: 1.5, color: INK }) } },
    ...[39, 26, 83, 148].map((n) => ({ text: String(n), options: { bold: true, align: "right", border: b(null, { pt: 1.5, color: INK }) } }))]);
  s.addTable(rows, { x: 0.6, y: 1.45, w: 8.4, colW: [2.7, 1.6, 1.6, 1.7, 0.8], fontSize: 16, color: INK, rowH: 0.62, valign: "middle", margin: [0, 0.1, 0, 0.1] });
  s.addShape(pres.shapes.LINE, { x: 9.35, y: 1.45, w: 0, h: 4.9, line: { color: LINE, width: 1 } });
  T(s, "제도환경", { x: 9.7, y: 1.45, w: 3.0, h: 0.5, fontSize: 16, bold: true });
  [["비MLS 포털·중개", "87"], ["MLS 시장", "53"], ["경매 시장", "4"], ["복수·불명", "4"]].forEach(([k, v], i) => {
    const yy = 2.05 + i * 0.6;
    T(s, k, { x: 9.7, y: yy, w: 2.2, h: 0.5, fontSize: 15 });
    T(s, v, { x: 11.9, y: yy, w: 0.8, h: 0.5, fontSize: 15, align: "right" });
    s.addShape(pres.shapes.LINE, { x: 9.7, y: yy + 0.55, w: 3.0, h: 0, line: { color: LINE, width: 1 } });
  });
  T(s, [{ text: "한국 관련 ", options: {} }, { text: "28", options: { bold: true, fontSize: 40 } }, { text: "편", options: {} }], { x: 9.7, y: 4.7, w: 3.0, h: 0.9, fontSize: 16, valign: "bottom" });
  s.addNotes([
    "주축은 거래 사슬 단계: 사람들이 관심을 갖고(S1), 매물이 나오고 호가가 붙고(S2), 매수자와 짝이 지어지고(S3), 거래가 체결되고(S4), 그 결과가 시장 전체 상태로 집계된다(S5).",
    "부축은 기능: 지표를 정의·구축했나(F1), 측정 문제를 다뤘나(F2), 다른 변수와의 선행성·관계를 봤나(F3).",
    "가장 큰 칸은 S4×F3 40편, 대부분 거래량–가격 선후행 연구이고 한국 논문 상당수가 여기 들어간다.",
    "배정표의 단계·기능·시장 코드는 초기값이다. 정리하면서 다르면 워드 '1. 분류'에 고치고 이유 한 줄.",
  ].join("\n"));
}

// 6. 정리 일정
{
  const s = pres.addSlide({ masterName: "CONTENT" });
  s.addText("정리 일정", { placeholder: "title" });
  s.addText("자료: students/assignments.csv(배정 v8, 2026-10-21). 매주 수요일 모임, 전날 화요일 18:00 마감", { placeholder: "source" });
  const W = [
    ["W01", "10/27", "1", "8", "한국"], ["W02", "11/03", "1", "8", "한국 S4"], ["W03", "11/10", "1", "8", "한국 S4·S1"], ["W04", "11/17", "1", "8", "한국 S1·S3"],
    ["W05", "11/24", "1", "8", "S3"], ["W06", "12/01", "2", "16", "S3"], ["W07", "12/08", "2", "16", "S2"], ["W08", "12/15", "2", "16", "S5"],
    ["W09", "12/22", "2", "16", "S4"], ["W10", "12/29", "2", "16", "S4"], ["W11", "01/05", "2", "15", "S1"], ["W12", "01/12", "1~2", "11", "원문 대기"],
  ];
  const lab = ["주차", "마감(화)", "1인 편수", "전체 편수", "내용"];
  const b = (top, bottom) => [top || { type: "none" }, { type: "none" }, bottom || { type: "none" }, { type: "none" }];
  const rows = lab.map((l, r) => {
    const first = r === 0, last = r === lab.length - 1;
    const bd = first ? b({ pt: 2, color: INK }, { pt: 1, color: INK }) : b(null, last ? { pt: 1.5, color: INK } : { pt: 1, color: LINE });
    return [{ text: l, options: { bold: true, border: bd, color: first ? INK : GRAY } },
      ...W.map((w) => ({ text: w[r], options: { bold: first, align: "center", border: bd, color: w[0] === "W12" ? ACC : INK } }))];
  });
  s.addTable(rows, { x: 0.6, y: 1.6, w: 12.1, colW: [1.3, ...Array(12).fill(0.9)], fontSize: 14, color: INK, rowH: 0.62, valign: "middle", margin: [0, 0.04, 0, 0.04] });
  // 기간 괘선 표시
  const colX = (i) => 0.6 + 1.3 + i * 0.9;
  [[0, 5, "청년 주거경로 리뷰 병행(주 1편)"], [5, 11, "주 2편"], [11, 12, "상호대차 후 배포"]].forEach(([a, z, t]) => {
    s.addShape(pres.shapes.LINE, { x: colX(a) + 0.08, y: 5.05, w: (z - a) * 0.9 - 0.16, h: 0, line: { color: GRAY, width: 1 } });
    T(s, t, a === 11 ? { x: 10.5, y: 5.15, w: 2.2, h: 0.4, fontSize: 12, color: GRAY, align: "right" } : { x: colX(a), y: 5.15, w: (z - a) * 0.9, h: 0.4, fontSize: 12, color: GRAY });
  });
  T(s, [{ text: "146", options: { bold: true, fontSize: 40 } }, { text: "편 · 12주 · 마지막 마감 2027.1.12", options: { fontSize: 16 } }], { x: 0.6, y: 5.75, w: 8, h: 0.9, valign: "bottom" });
  s.addNotes([
    "W1~W4는 한국 논문 27편부터(언어 부담이 없고 한국 시장 질문의 핵심). 그 뒤 영문을 단계 순으로: S3 매칭 → S2 호가 → S5 집계 → S4 체결 → S1 수요.",
    "W1~W5는 청년 주거경로 리뷰와 겹치는 기간이라 1인 1편, W6부터 2편.",
    "원문이 없거나 워킹페이퍼판만 있는 11편은 W12로 몰았다. 원석이 그 사이 상호대차·저자 메일로 구한다. 못 구하면 그 주는 비고 PRISMA에 '원문 확보 실패'로 기록.",
    "매주 수요일 모임에서 다음 논문을 받고, 다음 모임 전날 화요일 18:00까지 워드 1쪽 + 시트 행을 낸다. 학생 정리는 Claude가 따로 해 둔 정리와 대조해 다른 곳만 교수가 판정한다(독립 이중 추출).",
  ].join("\n"));
}

(async () => {
  await pres.writeFile({ fileName: OUT });
  await applyTheme(OUT, THEME);
  console.log("wrote", OUT);
})();
