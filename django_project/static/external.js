function copyToClipboard() {
  var text = document.getElementById("copy").textContent;
  if (text.trim() == "") {
    alert("복사할 키워드가 없습니다.");
    return;
  }
  var uniqueMatches = new Set();
  // 임시 textarea 엘리먼트 생성
  var textarea = document.createElement("textarea");
  text.match(/\(([^,]+),\d+\.\d+\)/g).forEach(function (match) {
    var matches = match.match(/\(([^,]+),\d+\.\d+\)/);
    if (matches) {
        for(let word of matches[1].split(' ')){
            uniqueMatches.add(word);
        }
    }
  });
  textarea.value = Array.from(uniqueMatches).join(", ");

  // textarea를 화면에 표시하지 않도록 스타일링
  textarea.style.position = "fixed";
  textarea.style.opacity = 0;

  // textarea를 문서에 추가
  document.body.appendChild(textarea);

  // textarea의 내용을 선택하고 복사
  textarea.select();

  document.execCommand("copy");

  // textarea 제거
  document.body.removeChild(textarea);

  // 복사 완료 메시지
  alert("키워드가 복사되었습니다: " + textarea.value);
}
