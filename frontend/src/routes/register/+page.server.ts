
export const actions = {
	create: async ({ request }) => {
        let headers= {Headers:{Authorization:'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImU0NzIzYjJmLTEyYTktNGVkNi1iYzVmLWU3M2Y5N2E0MTZhOSIsImVtYWlsIjoidW1pQGV4YW1wbGUuY29tIiwiZXhwIjoxNzMxMTMwNzMxfQ.SgTXI4yWImVuZydmAKtsMF5_UI3iYb9pFsgccAEzP8A'}}
        const general = await request.formData();
        let patient = {name:general.get('name'),
                      status: 1,
                      sex:parseInt(general.get('gender')),
                      birth_date:"2022-10-10", 
                      cpf:general.get('cpf'),
                      address_id:1
                    }

        let mock={
          name: "string",
          status: 0,
          sex: 0,
          birth_date: "2024-11-11",
          cpf: "stringstrin",
          address_id: 2
        }
        console.log(JSON.stringify(patient))
        const response = fetch('http://127.0.0.1:8000/api/patient/',{
          method: 'POST',
          headers: {Authorization:'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImU0NzIzYjJmLTEyYTktNGVkNi1iYzVmLWU3M2Y5N2E0MTZhOSIsImVtYWlsIjoidW1pQGV4YW1wbGUuY29tIiwiZXhwIjoxNzMxMzA2Nzc2fQ.zXPlkM_BtVMHVZltLCl2VJIIhzIZ-uWnWmmG0sMsfZ8','Content-Type': 'application/json'},
          body: JSON.stringify(patient)
      })
      return{success: true }
    }
};