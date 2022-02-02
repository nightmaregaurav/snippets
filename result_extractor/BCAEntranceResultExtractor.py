import sqlite3
import os
import weasyprint
import pdf2image

original_input = input


# noinspection PyShadowingBuiltins
def input(text, default):
    if __name__ == "__main__":
        return original_input(text)
    else:
        return default


def publish_result(year, campus_code, campus_name="", campus_address="", mode="2", action="N"):
    campus_code = str(campus_code)
    campus_name = str(campus_name)
    campus_address = str(campus_address)
    year = str(year)
    mode = str(mode)
    action = str(action)

    tu_rank = 0

    result_file = open("BCA_RESULT_ALL_RAW.txt")
    merit_list = [symbol_no.strip() for symbol_no in result_file]
    result_file.close()

    merit_set = set(merit_list)
    if len(merit_list) != len(merit_set):
        print(f"Total Repeated Symbol Numbers: {len(merit_list) - len(merit_set)}")
        print(f"Repeated Symbol Numbers: ")
        repeated = set([x for x in merit_list if merit_list.count(x) > 1])
        for sym in repeated:
            print(f"{sym}, ")

    year = input("Input Result Year: ", year)
    mode = input("Input 1 for New Single, 2 for Old Single, anything else for all: ", mode)

    campus_list = list()
    if mode == '1':
        campus_code = input("Input the symbol no of campus(eg. 02): ", campus_code)
        campus_name = input("Input the name campus(eg. Mechi Multiple Campus): ", campus_name)
        campus_address = input("Input the address campus(eg. Bhadrapur, Jhapa.): ", campus_address)
        campus_list.append({
            'campus_code': campus_code,
            'campus_name': campus_name,
            'campus_address': campus_address
        })
    elif mode == '2':
        campus_code = input("Input the symbol no of campus(eg. 02): ", campus_code)
        conn = sqlite3.connect('campus.db')
        # noinspection SqlDialectInspection,SqlNoDataSourceInspection
        cursor = conn.execute(f"SELECT name, address from campus WHERE code = '{campus_code}'")
        row = cursor.fetchone()
        if row is None:
            print("Given campus code does not exist in database.")
            exit(1)
        campus_name = row[0]
        campus_address = row[1]
        campus_list.append({
            'campus_code': campus_code,
            'campus_name': campus_name,
            'campus_address': campus_address
        })
    else:
        conn = sqlite3.connect('campus.db')
        # noinspection SqlDialectInspection,SqlNoDataSourceInspection
        cursor = conn.execute("SELECT code, name, address from campus")
        for row in cursor:
            campus_code = row[0]
            campus_name = row[1]
            campus_address = row[2]
            campus_list.append({
                'campus_code': campus_code,
                'campus_name': campus_name,
                'campus_address': campus_address
            })

    analysed_symbol_nos = set()
    print()
    for campus in campus_list:
        campus_code = campus['campus_code']
        campus_name = campus['campus_name']
        campus_name = " ".join(campus_name.replace(" ,", ",").replace(",", ", ").split()).title()
        campus_address = campus['campus_address']
        campus_address = " ".join(campus_address.replace(" ,", ",").replace(",", ", ").split()).title()

        text_file_content = f"BCA Entrance Result: {year}\n" \
                            f"Campus: {campus_name}\n" \
                            f"Address: {campus_address}\n" \
                            f"Code: {campus_code}\n"
        html_file_content = "<!DOCTYPE html>\n" \
                            "<html>\n" \
                            "<head>\n" \
                            f"	<title>{campus_code} BCA Entrance Result: {year}</title>\n" \
                            "</head>\n" \
                            "<body>\n" \
                            "	<center>\n" \
                            "		<table border='2px' style='margin-left: auto; margin-right: auto;'>\n" \
                            "			<thead>\n" \
                            "				<tr>\n" \
                            "					<th colspan='3'>\n" \
                            f"						BCA Entrance Result: {year}\n" \
                            "					</th>\n" \
                            "				</tr>\n" \
                            "				<tr>\n" \
                            "					<th colspan='3'>\n" \
                            f"						Campus: {campus_name}\n" \
                            "					</th>\n" \
                            "				</tr>\n" \
                            "				<tr>\n" \
                            "					<th colspan='3'>\n" \
                            f"						Address: {campus_address}\n" \
                            "					</th>\n" \
                            "				</tr>\n" \
                            "				<tr>\n" \
                            "					<th colspan='3'>\n" \
                            f"						Code: {campus_code}\n" \
                            "					</th>\n" \
                            "				</tr>\n" \
                            "				<tr>\n" \
                            "					<th colspan='3'>\n" \
                            "						" \
                            "					</th>\n" \
                            "				</tr>\n" \
                            "				<tr>\n" \
                            "					<th>\n" \
                            "						| All Nepal Rank |\n" \
                            "					</th>\n" \
                            "					<th>\n" \
                            "						| Campus Rank |\n" \
                            "					</th>\n" \
                            "					<th>\n" \
                            "						| Symbol No |\n" \
                            "					</th>\n" \
                            "				</tr>\n" \
                            "			</thead>\n" \
                            "			<tbody>\n"
        post_file_content = text_file_content
        post_file_content += "PDF Link: <<replace_me>>\n"
        text_file_content += "\nAllNepalRank\t CampusRank\t SymbolNo\n"

        tu_rank = 0
        campus_rank = 0

        for symbol_no in merit_set:
            tu_rank += 1
            campus_code_src = int(symbol_no.split("-")[0])
            campus_code_dest = int(campus_code)
            if campus_code_dest == campus_code_src:
                campus_rank += 1
                analysed_symbol_nos.add(symbol_no)
                text_file_content += f"{tu_rank}\t {campus_rank}\t {symbol_no}\n"
                html_file_content += "<tr>\n" \
                                     f"	<td>{tu_rank}</td>\n" \
                                     f"	<td>{campus_rank}</td>\n" \
                                     f" <td>{symbol_no}</td>\n" \
                                     "</tr>\n"

        html_file_content += "			</tbody>\n" \
                             "          <tfoot>\n" \
                             "            <tr><td colspan='3'></td></tr>\n" \
                             "            <tr><td colspan='3'></td></tr>\n" \
                             "            <tr>\n" \
                             "                <td colspan='3' style='text-align: center;'><small><i>Extracted by: <b>Gaurav Nyaupane (MMC BCA 2017)</b></i><small></td>\n" \
                             "            </tr>\n" \
                             "          </tfoot>\n" \
                             "		</table>\n" \
                             "	</center>\n" \
                             "</body>\n" \
                             "</html>\n"
        post_file_content += f"Total Passed student(TU): {tu_rank}\n" \
                             f"Total Passed student(This Campus): {campus_rank}\n\n" \
                             f"Search your campus' result using hashtag<campus code>(eg. #BCA{year}TU_{campus_code})\n" \
                             f"If result for your campus is not published, inbox us your campus' code/symbol no to get it published.\n" \
                             f"#BCA #EntranceResult{year} #BCATU\n\n" \
                             f"Extracted By: Gaurav Nyaupane (MMC BCA 2017)"
        text_file_content += f"\nTotal Passed student(TU): {tu_rank}" \
                             f"\nTotal Passed student(This Campus): {campus_rank}" \
                             f"\n\nExtracted By: Gaurav Nyaupane (MMC BCA 2017)"
        print(f"Total Passed Students in ({campus_code}) {campus_name}, {campus_address}: {campus_rank}")

        os.makedirs("result_outputs", exist_ok=True)
        os.makedirs("result_outputs_post_files", exist_ok=True)
        post_file = open(f"result_outputs_post_files/{campus_code}_post_file.txt", "w")
        text_file = open(f"result_outputs/{campus_code}.txt", "w")
        html_file = open(f"result_outputs/{campus_code}.html", "w")

        post_file.write(post_file_content)
        text_file.write(text_file_content)
        html_file.write(html_file_content)

        post_file.close()
        text_file.close()
        html_file.close()

        weasyprint.HTML(f'result_outputs/{campus_code}.html').write_pdf(f'result_outputs/{campus_code}.pdf')

        os.makedirs(f"result_outputs_post_files/{campus_code}", exist_ok=True)
        images = pdf2image.convert_from_path(f'result_outputs/{campus_code}.pdf')
        for i in range(len(images)):
            images[i].save(f'result_outputs_post_files/{campus_code}/Page {i+1}.jpg', "JPEG")

    if mode != '1' and mode != '2':
        print(f"\nTotal Unique Symbol Numbers: {tu_rank}")
        print(f"Total Analysed Symbol Numbers: {len(analysed_symbol_nos)}")
        not_analysed = merit_set - analysed_symbol_nos
        if len(not_analysed) > 0:
            print(f"You are missing campus codes in db for {len(not_analysed)} entries:")
            for sym in not_analysed:
                print(f"{sym}")

    print(f"\n\nDear admin, \n"
          f"Upload PDF, HTML, and TXT files of campus' result which are inside 'result_outputs' folder of your current directory to google drive.\n"
          f"Share the files so anyone with the link may access them.\n"
          f"Copy the PDF links of each PDFs.\n"
          f"Replace <<replace_me>> in fifth line of 'result_outputs_post_files/{campus_code}_post_file.txt with the link copied for corresponding files to PDF.\n"
          f"Copy and paste whatever is in 'result_outputs_post_files/{campus_code}_post_file.txt' and post it in the facebook page after attaching photos in 'result_outputs_post_files/{campus_code}' folder of your current directory.\n"
          f"'.\n\n\tRegards\n\t-Gaurav Nyaupane\n\n")

    if mode == '1':
        conn = sqlite3.connect('campus.db')
        # noinspection SqlDialectInspection,SqlNoDataSourceInspection
        cursor = conn.execute(f"SELECT COUNT(*) FROM campus where code = '{campus_code}'")
        count = cursor.fetchone()[0]

        if count == 0:
            action = input("Do you want to save this campus? (Y for yes): ", action)
        else:
            action = input("Do you want to update this campus with new details? (Y for yes): ", action)

        if action.lower() == 'y':
            if count == 0:
                # noinspection SqlDialectInspection,SqlNoDataSourceInspection
                conn.execute(f"INSERT INTO campus(code,name,address) VALUES('{campus_code}', '{campus_name}','{campus_address}')")
            else:
                # noinspection SqlDialectInspection,SqlNoDataSourceInspection
                conn.execute(f"UPDATE campus SET name = '{campus_name}', address = '{campus_address}' WHERE code = '{campus_code}'")

            conn.commit()

        conn.close()


if __name__ == "__main__":
    publish_result("", "")
