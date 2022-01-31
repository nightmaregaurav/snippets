import sqlite3
import os
import weasyprint
import pdf2image

result_file = open("BCA_RESULT_ALL_RAW.txt")
merit_list = [symbol_no.strip() for symbol_no in result_file]
result_file.close()

year = input("Input Result Year: ")

mode = input("Input 1 for Single, anything else for all: ")
campus_list = list()
if mode == '1':
    campus_code = input("Input the symbol no of campus(eg. 02): ")
    campus_name = input("Input the name campus(eg. Mechi Multiple Campus): ")
    campus_address = input("Input the address campus(eg. Bhadrapur, Jhapa.): ")
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
        campus_list.append({
            'campus_code': row[0],
            'campus_name': row[1],
            'campus_address': row[2]
        })

for campus in campus_list:
    campus_code = campus['campus_code']
    campus_name = campus['campus_name']
    campus_name = " ".join(campus_name.replace(" ,", ",").replace(",", ", ").split()).title()
    campus_address = campus['campus_address']
    campus_address = " ".join(campus_address.replace(" ,", ",").replace(",", ", ").split()).title()

    print("\n\n\tAllNepalRank\tCampusRank\t SymbolNo\n")
    print("-------------------------------------------\n\n")
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

    for symbol_no in merit_list:
        tu_rank += 1
        campus_code_src = int(symbol_no.split("-")[0])
        campus_code_dest = int(campus_code)
        if campus_code_dest == campus_code_src:
            campus_rank += 1
            print(f"\t {tu_rank}\t {campus_rank}\t {symbol_no}\n")

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

    text_file_content += "\n\n\nExtracted By: Gaurav Nyaupane (MMC BCA 2017)"

    os.makedirs("result_outputs", exist_ok=True)
    post_file = open(f"{campus_code}_post_file.txt", "w")
    text_file = open(f"result_outputs/{campus_code}.txt", "w")
    html_file = open(f"result_outputs/{campus_code}.html", "w")

    post_file.write(post_file_content)
    text_file.write(text_file_content)
    html_file.write(html_file_content)

    post_file.close()
    text_file.close()
    html_file.close()

    weasyprint.HTML(f'result_outputs/{campus_code}.html').write_pdf(f'result_outputs/{campus_code}.pdf')

    os.makedirs(f"{campus_code}", exist_ok=True)
    images = pdf2image.convert_from_path(f'result_outputs/{campus_code}.pdf')
    for i in range(len(images)):
        images[i].save(f'{campus_code}/Page {i}.jpg', "JPEG")

    print(f"\nDear admin, \n"
          f"Upload PDF, HTML, and TXT files of campus' result which are inside 'result_outputs' folder of your current directory to google drive.\n"
          f"Share the files so anyone with the link may access them.\n"
          f"Copy the PDF link.\n"
          f"Replace <<replace_me>> in fifth line of '{campus_code}_post_file.txt with the link copied.\n"
          f"Copy and paste whatever is in '{campus_code}_post_file.txt' and post it in the facebook page after attaching photos in {campus_code} folder of your current director.\n"
          f"'.\n\n\tRegards\n\t-Gaurav Nyaupane\n\n")

    if mode == '1':
        conn = sqlite3.connect('campus.db')
        # noinspection SqlDialectInspection,SqlNoDataSourceInspection
        cursor = conn.execute(f"SELECT COUNT(*) FROM campus where code = '{campus_code}'")
        count = cursor.fetchone()[0]

        if count == 0:
            action = input("Do you want to save this campus? (Y for yes): ")
        else:
            action = input("Do you want to update this campus with new details? (Y for yes): ")

        if action.lower() == 'y':
            if count == 0:
                # noinspection SqlDialectInspection,SqlNoDataSourceInspection
                conn.execute(f"INSERT INTO campus(code,name,address) VALUES('{campus_code}', '{campus_name}','{campus_address}')")
            else:
                # noinspection SqlDialectInspection,SqlNoDataSourceInspection
                conn.execute(f"UPDATE campus SET name = '{campus_name}', address = '{campus_address}' WHERE code = '{campus_code}'")

            conn.commit()

        conn.close()
