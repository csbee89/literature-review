// 유동성 리뷰 논문 정리 Word 양식(빈 양식) + 예시 2편. 청년 주거경로 리뷰 양식(2026-10-14)과 같은 구조.
// 사용: node scripts/make_word.js  → handover/word/*.docx
const fs = require('fs');
const path = require('path');
const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType, ShadingType, BorderStyle } = require('docx');

const OUT = path.join(__dirname, '..', 'handover', 'word');
fs.mkdirSync(OUT, { recursive: true });
const FONT = '맑은 고딕';
const GRAY = '777777';
const W = 9026; // A4 본문 폭(DXA)

const run = (t, o = {}) => new TextRun({ text: t, font: FONT, size: o.size || 20, bold: !!o.bold, italics: !!o.italics, color: o.color });
const para = (children, o = {}) => new Paragraph({ children: Array.isArray(children) ? children : [children], spacing: { before: o.before || 0, after: o.after == null ? 80 : o.after, line: 276 } });
const h = (t) => new Paragraph({ children: [run(t, { bold: true, size: 22 })], spacing: { before: 200, after: 80 }, border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: 'BFC8D2', space: 2 } } });
const bd = { style: BorderStyle.SINGLE, size: 4, color: 'BFC8D2' };
function cell(text, width, o = {}) {
  return new TableCell({
    width: { size: width, type: WidthType.DXA },
    shading: o.fill ? { type: ShadingType.CLEAR, fill: o.fill, color: 'auto' } : undefined,
    borders: { top: bd, bottom: bd, left: bd, right: bd },
    margins: { top: 60, bottom: 60, left: 100, right: 100 },
    children: [para(run(text, { bold: o.bold, color: o.color, italics: o.italics, size: o.size || 19 }), { after: 0 })],
  });
}
const table = (rows, widths) => new Table({ width: { size: widths.reduce((a, b) => a + b, 0), type: WidthType.DXA }, columnWidths: widths, rows: rows.map(r => new TableRow({ children: r })) });

// 분류 항목: [라벨, 선택지 안내]
const CLASS = [
  ['단계', 'S1 수요·관심 / S2 공급·호가 설정 / S3 매칭 / S4 체결·가격 발견 / S5 집계 상태 (배정표 값이 맞는지 확인)'],
  ['기능', 'F1 정의·구축 / F2 측정 쟁점 / F3 선행성·관계'],
  ['시장', 'MLS / 비MLS 포털·중개 / 경매'],
  ['지표', '지표 이름과 정의 한 줄 (쪽)'],
  ['결과', '지표가 무엇과 어떤 방향으로 관련되나. 몇 개월 앞서나 (쪽)'],
  ['국가 · 자료', '나라·지역, 자료 이름, 기간 (쪽)'],
  ['표본', '매물 수·거래 수·월 수 등 (쪽)'],
  ['분석 방법', '모형 이름 (쪽)'],
];

function build(d, file) {
  const blank = !d; d = d || {};
  const v = (k, hint) => (blank ? hint : d[k]);
  const g = blank ? { color: GRAY, italics: true } : {};
  const children = [
    para(run('주택시장 유동성 지표 리뷰 · 논문 정리', { bold: true, size: 28 }), { after: 40 }),
    para(run(blank ? '한 쪽 안팎. 칸마다 괄호 안에 쪽수. 논문에 없으면 「보고 안 됨」, 해당 없으면 「해당 없음」. 숫자와 세부 항목은 구글시트에 채운다.' : d.note, { color: GRAY, size: 18 }), { after: 160 }),
    table([[
      cell('정리자', 1300, { fill: 'E8EEF4', bold: true }), cell(v('who', ''), 2213),
      cell('주차', 900, { fill: 'E8EEF4', bold: true }), cell(v('week', ''), 1100),
      cell('논문 번호', 1300, { fill: 'E8EEF4', bold: true }), cell(v('pid', 'p###'), 2213, blank ? { color: GRAY } : {}),
    ]], [1300, 2213, 900, 1100, 1300, 2213]),
    h('서지'),
    para(run(v('cite', '저자 (연도). 제목. 학술지 권(호), 쪽. DOI'), g)),
    h('1. 분류'),
    table(CLASS.map(([k, hint], i) => [cell(k, 1700, { fill: 'F2F2F2', bold: true }), cell(blank ? hint : d.cls[i], W - 1700, blank ? { color: GRAY, italics: true } : {})]), [1700, W - 1700]),
    h('2. 요약'),
    para(run(blank ? '4~6문장. 무엇을 물었나 → 어떤 자료 → 어떤 방법 → 무엇을 찾았나(핵심 숫자 한두 개) → 저자 결론. 문장마다 쪽수.' : d.summary.join(' '), g)),
    h('3. 저자가 적은 한계'),
    ...(blank ? ['논문에 적힌 한계를 1~3개. 없으면 「적힌 한계 없음」.'] : d.limits).map(s => para(run(blank ? s : '· ' + s, g), { after: 40 })),
    h('4. 읽으면서 막힌 것'),
    ...(blank ? ['이해가 안 된 표, 숫자가 안 맞는 곳, 애매한 용어, 저자 문장과 표가 다른 곳. 비워두지 않는다.'] : d.stuck).map(s => para(run(blank ? s : '· ' + s, g), { after: 40 })),
  ];
  const doc = new Document({ styles: { default: { document: { run: { font: FONT, size: 20 } } } }, sections: [{ properties: { page: { margin: { top: 1000, bottom: 1000, left: 1100, right: 1100 } } }, children }] });
  return Packer.toBuffer(doc).then(b => fs.writeFileSync(path.join(OUT, file), b));
}

const P115 = {
  note: '예시(국문 학술지). 이 정도 길이와 깊이로 쓰면 된다. 숫자와 세부 항목은 구글시트 예시 행에 있다.', who: '(예시)', week: '예시', pid: 'p115',
  cite: '마승렬 (2021). 빈도영역 분석법을 통한 주택가격과 거래량의 공통 사이클 분석(Frequency domain analysis to detect common cycle in housing price and trading volume). 주택도시금융연구 6(2), 53–73. doi:10.38100/jhuf.2021.6.2.53',
  cls: [
    'S4 체결·가격 발견 (배정표와 같음)',
    'F3 선행성·관계',
    '비MLS 포털·중개 (한국, 집계 거래량만 사용)',
    '아파트 거래량. "the twelvemonth accumulated monthly apartment trading volume"을 HP 필터로 추세 제거 후 표준화 (57, 각주 3)',
    '거래량이 가격상승률보다 약간 앞섬. 전국 48개월 주기에서 약 3개월, 20개월 주기에서 약 1.9개월 (61). 비수도권은 선행 판단 불가 (67)',
    '한국 4개 권역, 한국부동산원 월별 아파트 가격지수·거래량, 2007.01~2018.10 (57)',
    '월별 시계열 약 142개월 × 4권역. 관측치 수는 보고 안 됨 (57)',
    '스펙트럼 분석(periodogram, 교차스펙트럼), 조화분석, Granger 인과 검정, VAR(2~4) (55–56, 60, 64)',
  ],
  summary: [
    '이 논문은 주택가격과 거래량에 공통 주기가 있는지, 그 주기에서 무엇이 먼저 움직이는지 묻는다 (53–55).',
    '한국부동산원의 월별 아파트 가격지수 전년동월비와 12개월 누적 거래량을 4개 권역으로 나눠 썼다 (57).',
    '두 시계열을 HP 필터로 추세 제거·표준화한 뒤 스펙트럼 분석으로 주기를 찾고, Granger 검정과 VAR로 시간 영역 결과와 비교했다 (57–60).',
    '공통 주기는 20개월(광역시는 24개월)과 48개월이었고, 교차스펙트럼의 결맞음은 0.58~0.87이었다 (61, 표 3·4).',
    '저자는 주기 영역에서 거래량이 가격상승률보다 약간 앞서며, Granger 검정상 양방향 인과가 있다고 결론짓는다 (60–61, 68).',
  ],
  limits: [
    '자료가 2018년 10월까지라 새 자료로 주기적으로 다시 분석해야 한다 (69).',
    '금리 등 다른 변수를 함께 보는 분석이 필요하다 (69).',
  ],
  stuck: [
    '저자는 "지역과 관계없이 양방향 인과"라고 썼지만(60), 표 2를 보면 가격→거래량은 대부분 시차에서 유의하고 거래량→가격은 짧은 시차(2~3개월)에서만 유의하다.',
    '표 4에 "SMetro"가 두 번 나온다. 두 번째 행은 순서상 비수도권(NMetro)으로 보인다 (62).',
    '저자는 위상을 개월로 바꿀 때 위상÷π×주기를 썼다(61). 흔히 쓰는 위상÷2π×주기로 계산하면 약 1.5개월·0.95개월로 절반이 된다. 위상 단위가 적혀 있지 않아 어느 쪽이 맞는지 판단 못 함.',
    '거래량이 신고 기준인지 등기 기준인지, 가격지수가 동향조사 지수인지 실거래가격지수인지 보고 안 됨 (57).',
  ],
};

const P033 = {
  note: '예시(영문 학술지). 이 정도 길이와 깊이로 쓰면 된다. 숫자와 세부 항목은 구글시트 예시 행에 있다.', who: '(예시)', week: '예시', pid: 'p033',
  cite: 'Liu, Y., Shakib, S., Miller, E. J., & Habib, K. N. (2024). Modeling home property listings’ time-on-market duration and listing outcome using copula-based competing risk method. Journal of Transport and Land Use 17(1), 579–601. doi:10.5198/jtlu.2024.2447',
  cls: [
    'S3 매칭 (배정표와 같음)',
    'F2 측정 쟁점 (팔리지 않고 내려간 매물을 경쟁위험으로 함께 모형화)',
    'MLS (토론토 부동산협회 TRREB 매물 자료, 583)',
    'TOM. "the days between the listing date and the sale or termination date of a residential property" (580). 종료일은 팔리거나 내려가 비활성이 된 날 (580)',
    '호가가 높을수록 TOM이 길어짐(로그 호가 계수 0.74~0.78, 표 2, 592). 선행성은 다루지 않음',
    '캐나다 토론토 광역권(GTA), TRREB 매물 자료, 2021년 첫 등록 매물 (583)',
    '첫 등록 매물 18,272건. 50%가 첫 등록에서 팔림 (583)',
    '중첩 로짓(결과 4가지) + 경쟁위험 로그정규 가속실패시간 모형(TOM)을 Gumbel 코퓰라로 결합 (586–590)',
  ],
  summary: [
    '이 논문은 매물이 얼마나 오래 시장에 있다가 팔리거나 내려가는지, 내려간 뒤 판매자가 무엇을 하는지 묻는다 (580).',
    '2021년 토론토 광역권에 처음 등록된 매물 18,272건을 쓰고, 결과를 판매·철회·임대 전환·재등록의 넷으로 나눴다 (583).',
    '결과 선택은 중첩 로짓, TOM은 판매와 종료를 경쟁위험으로 둔 로그정규 가속실패시간 모형으로 추정하고, 둘을 Gumbel 코퓰라로 묶었다 (586–590).',
    '세 종료 선택 모두 코퓰라 모수가 1보다 커서(1.16, 1.14, 1.72) 종료 결정과 TOM 사이에 관측되지 않은 요인의 상관이 있었다 (표 1, 591).',
    '호가가 높을수록 TOM이 길고 종료 확률이 높았으며, 종료된 매물의 약 70%는 같은 해에 다시 매물로 나왔다 (592, 596).',
  ],
  limits: [
    '판매자에 대한 정보가 없어 판매자 특성을 넣지 못했다 (599).',
    '경쟁 결과가 조건부인 모형 등 다른 구조와 비교하지 못했다 (599).',
    '2021년은 코로나19 중 토론토 시장이 이례적으로 활발했던 해라 일반화에 한계가 있다 (599).',
  ],
  stuck: [
    '코퓰라 상관의 해석이 앞뒤가 다르다. 초록과 591쪽은 "종료 확률을 높이는 요인이 TOM을 줄인다", 결론(598)은 "TOM을 늘린다"고 쓴다.',
    'TOM은 첫 등록 매물 기준이라 재등록 뒤의 기간은 이어 붙이지 않았다(583). 재등록을 같은 매물로 보면 TOM이 더 길어질 것이다.',
    '표 2는 로그 TOM에 대한 계수라 양수면 TOM이 길어진다는 뜻으로 읽었다(588). 계수의 단위가 표에 따로 적혀 있지 않다.',
    '본문의 식 번호가 하나씩 어긋난다(예: 코퓰라 식을 "Equation 12"라고 부르지만 식 13).',
  ],
};

(async () => {
  await build(null, '논문정리_양식_v1.docx');
  await build(P115, '예시_p115_마승렬2021.docx');
  await build(P033, '예시_p033_Liu2024.docx');
  console.log('written to', OUT);
})();
