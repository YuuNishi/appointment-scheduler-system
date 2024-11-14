
export const actions = {
	create: async ({ request }) => {
        let headers= {Headers:{Authorization:'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImU0NzIzYjJmLTEyYTktNGVkNi1iYzVmLWU3M2Y5N2E0MTZhOSIsImVtYWlsIjoidW1pQGV4YW1wbGUuY29tIiwiZXhwIjoxNzMxMTMwNzMxfQ.SgTXI4yWImVuZydmAKtsMF5_UI3iYb9pFsgccAEzP8A'}}
        const general = await request.formData();
        let cep = general.get('cep')
        cep = cep.replace('-','')
        let address = {
          cep: cep,
          street: general.get('street'),
          neighborhood: general.get('neighborhood'),
          city: general.get('city'),
          federal_unit: general.get('state'),
          number: parseInt(general.get('number'))
        }
        async function newAddress(address){
          let add_id 
          await fetch('http://127.0.0.1:8000/api/address/',{
            method: 'POST',
            headers: {Authorization:'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImU0NzIzYjJmLTEyYTktNGVkNi1iYzVmLWU3M2Y5N2E0MTZhOSIsImVtYWlsIjoidW1pQGV4YW1wbGUuY29tIiwiZXhwIjoxNzMxNTYxNDE5fQ.LS8M3-q66JhZ_rMAR2CJ6-i5sonV4dE42HqO2PL68Nk','Content-Type': 'application/json'},
            body: JSON.stringify(address)
          }).then(resp=>resp.json()).then(data=>{add_id =data.id ;})
          return add_id
        }
        let id = await newAddress(address)
        
        let patient = {name:general.get('name'),
          status: 1,
          sex:parseInt(general.get('gender')),
          birth_date:"2024-11-11", 
          cpf:general.get('cpf'),
          address_id:id
        }
        async function addPatient(patient) {
          const response2 = fetch('http://127.0.0.1:8000/api/patient/',{
          method: 'POST',
          headers: {Authorization:'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImU0NzIzYjJmLTEyYTktNGVkNi1iYzVmLWU3M2Y5N2E0MTZhOSIsImVtYWlsIjoidW1pQGV4YW1wbGUuY29tIiwiZXhwIjoxNzMxNTYxNDE5fQ.LS8M3-q66JhZ_rMAR2CJ6-i5sonV4dE42HqO2PL68Nk','Content-Type': 'application/json'},
          body: JSON.stringify(patient)
          })
        }
        await addPatient(patient)
      return{success: true }
    },
};